import pytest

from api import create_app

app = create_app()


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


# Todo: create mocked geo, and weather apis to avoid call them while testing
def test_when_get_home_then_get_welcome_message(client):
    # Act
    rv = client.get('/')

    # Assert
    assert b'Weather API' in rv.data


def test_when_post_temperature_given_address_then_get_temperature_and_city(client):
    # Arrange
    data = dict(address='new york city')

    # Act
    rv = client.post('/api/temperature', data=data)

    # Assert
    assert b'city' in rv.data
    assert b'temp' in rv.data
    assert 'New York, US' == rv.get_json()['city']


def test_when_post_temperature_given_non_existent_address_then_get_temperature_and_city_empty(client):
    # Arrange
    data = dict(address='------')

    # Act
    rv = client.post('/api/temperature', data=data)

    # Assert
    assert b'city' in rv.data
    assert b'temp' in rv.data
    assert '' == rv.get_json()['temp']
    assert 'Not found address' == rv.get_json()['city']


def test_when_post_temperature_given_an_empty_address_then_get_temperature_and_city_empty(client):
    # Arrange
    data = dict(address='')

    # Act
    rv = client.post('/api/temperature', data=data)

    # Assert
    assert 400 == rv.status_code
    assert b'address parameter not found in form data' in rv.response


def test_when_post_temperature_given_a_wrong_data_param_then_bad_request_status_code(client):
    # Arrange
    data = dict(typoParam='')

    # Act
    rv = client.post('/api/temperature', data=data)

    # Assert
    assert 400 == rv.status_code
    assert b'address parameter not found in form data' in rv.response

