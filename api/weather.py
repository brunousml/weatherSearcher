import os

import requests
from flask import (
    Blueprint, request, jsonify
)

# Todo: enable versions to api
bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/temperature', methods=['POST'])
def temperature():
    # todo: add authentication, and validations to this route
    # todo: check if it already exists in cache
    # todo: set cache invalidation to 1 hour
    # todo: store cache, and logs

    # todo: add validation to address field on the form
    data = request.form
    result = {
        'city': 'Not found address',
        'temp': '',
    }

    if 'address' in data and data['address']:
        geometry = get_geometry_locations(data['address'])
        if len(geometry) >= 2:
            result['city'] = geometry['city']
            temp = get_temperature_by_geometry(geometry['geo'])
            result['temp'] = "{0}° C".format(round(temp['temp']))

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
    return weather_r.json()['main']
