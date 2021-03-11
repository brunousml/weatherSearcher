import json
import os
import datetime

import requests
from flask import (
    Blueprint, request, jsonify
)

# Todo: enable versions to api
bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/temperature', methods=['POST'])
def temperature():
    # todo: add authentication, and validations to this route
    # todo: store cache, and logs

    from api.manager import Address, db
    data = request.form
    result = {
        'city': 'Not found address',
        'temp': '',
    }

    if 'address' in data and data['address']:
        # Get geo
        geometry = get_geometry_locations(data['address'])
        if len(geometry) >= 2:
            result['city'] = geometry['city']

            # Check if was already added to the database
            cached = Address.query.filter_by(address=geometry['city']).first()
            if cached:
                # set cached values
                result['city'] = cached.address
                result['temp'] = cached.temperature

                # Assume the temperature for a Zipcode does not vary within 1-hour window
                is_cache_invalid = not (cached.updated + datetime.timedelta(hours=1)) >= datetime.datetime.utcnow()
                if is_cache_invalid:  # if not valid, update it
                    # I choose using lat, lng because some places do not have zipcode, it limits the search
                    temp = get_temperature_by_geometry(geometry['geo'])
                    result['temp'] = "{0}° C".format(round(temp['temp']))

                    # Todo: encapsulate it
                    cached.temperature = result['temp']
                    db.session.add(cached)
                    db.session.commit()
            else:
                # Todo: encapsulate it
                address_model = Address(
                    address=result['city'],
                    geo=json.dumps(geometry['geo']),
                    temperature=result['temp'],
                )
                db.session.add(address_model)
                db.session.commit()
    else:
        return "address parameter not found in form data", 400

    return jsonify(result)


def get_geometry_locations(address):
    geo_key = os.environ['GEOCODE_API_KEY']
    # Todo: move this url to an environ variable
    geo_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}'.format(
        address=address,
        key=geo_key
    )
    geo_r = requests.get(geo_url)
    result = {}
    # Get country
    if len(geo_r.json()['results']) > 0:
        geo_data = geo_r.json()['results'][0]
        country = ''
        adm_area = ''
        for el in geo_data['address_components']:
            if 'country' in el['types']:
                country = el['short_name']
            if 'administrative_area_level_1' in el['types']:
                adm_area = el['long_name']

        result = dict(
            city="{0}, {1}".format(adm_area, country),
            geo=geo_data['geometry']['location']
        )

    return result


def get_temperature_by_geometry(geometry):
    weather_key = os.environ['WEATHER_API_KEY']
    # Todo: move this url to an environ variable
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}'.format(
        lat=geometry['lat'],
        lon=geometry['lng'],
        key=weather_key
    )
    weather_r = requests.get(weather_url)
    if weather_r.status_code >= 400:
        raise Exception('WeatherAPI: Invalid api key')
    return weather_r.json()['main']
