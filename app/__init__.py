import hashlib
import json
import os

import requests
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models.address_model import AddressModel


@app.route('/')
def index():
    return 'Welcome back!'


@app.route('/weather', methods=['POST'])
def weather():
    data = request.form
    # todo: check if it exists in cache
    # todo: set cache invalidation
    # Getting geo data
    geometry = get_geometry_locations(data['address'])

    # Getting weather data
    temperature = get_temperature_by_geometry(geometry)

    # todo: save logs, and address
    return jsonify(temperature)


def save_weather_address(address, geometry, temperature):
    hash_address = hashlib.md5(address.encode(encoding='UTF-8', errors='strict')).digest()
    geo = json.dumps(geometry)
    address_model = AddressModel(
        address=hash_address,
        zipcode=geo,
        temperature=temperature
    )
    db.session.add(address_model)
    db.session.commit()


def get_geometry_locations(address):
    # Todo: move this key to an environment variable
    geo_key = 'AIzaSyD7cS6Q4zctxzUqZJpBdSQxVSGwrSmxVCI'
    geo_url = 'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}'.format(
        address=address,
        key=geo_key
    )
    geo_r = requests.get(geo_url)
    return geo_r.json()['results'][0]['geometry']['location']


def get_temperature_by_geometry(geometry):
    # Todo: move this key to an environment variable
    weather_key = '9e671ceeb75351872365df4a78c72488'
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}'.format(
        lat=geometry['lat'],
        lon=geometry['lng'],
        key=weather_key
    )
    weather_r = requests.get(weather_url)
    return weather_r.json()['main']


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
