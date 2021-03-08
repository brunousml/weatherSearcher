import os

import requests
from flask import (
    Blueprint, request, jsonify
)

# Todo: enable versions to api
bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/temperature', methods=['POST'])
def temperature():
    data = request.form
    # todo: check if it exists in cache
    # todo: set cache invalidation
    # todo: save address, and logs

    # Getting geo data
    geometry = get_geometry_locations(data['address'])

    # Getting weather data
    temp = get_temperature_by_geometry(geometry)

    return jsonify(temp)


def get_geometry_locations(address):
    geo_key = os.environ['GEOCODE_API_KEY']
    geo_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}'.format(
        address=address,
        key=geo_key
    )
    geo_r = requests.get(geo_url)
    return geo_r.json()['results'][0]['geometry']['location']


def get_temperature_by_geometry(geometry):
    weather_key = os.environ['WEATHER_API_KEY']
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}'.format(
        lat=geometry['lat'],
        lon=geometry['lng'],
        key=weather_key
    )
    weather_r = requests.get(weather_url)
    return weather_r.json()['main']
