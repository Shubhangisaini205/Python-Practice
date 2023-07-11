import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_display_weather_valid_city(client):
    city = 'New York'
    # expected_data = {'temperature': 25, 'weather': 'Sunny'}
    expected_data = {
        'temperature': 20,
        'weather': 'Sunny'
    }

    response = client.get(f'/weather/{city}')
    assert response.status_code == 200
    assert response.json == expected_data


def test_display_weather_invalid_city(client):
    city = 'NonexistentCity'
    response = client.get(f'/weather/{city}')
    assert response.status_code == 400
    assert response.json == {'error': 'City not found'}


def test_post_weather_valid_data(client):
    data = {
        'city': 'London',
        'temperature': 25,
        'weather': 'Sunny'
    }
    expected_response = {'message': 'Weather data added successfully'}

    response = client.post('/weather', json=data)
    assert response.status_code == 200
    assert response.json == expected_response


def test_post_weather_invalid_data(client):
    data = {
        'temperature': 25,
        'weather': 'Sunny'
    }
    expected_response = {'error': 'Invalid data'}

    response = client.post('/weather', json=data)
    assert response.status_code == 400
    assert response.json == expected_response


def test_put_weather_valid_data(client):
    city = 'London'
    data = {
        'temperature': 25,
        'weather': 'Sunny'
    }
    expected_response = {'message': 'Weather data updated!!!'}

    response = client.put(f'/weather/{city}', json=data)
    assert response.status_code == 200
    assert response.json == expected_response


def test_put_weather_invalid_data(client):
    city = 'NonexistentCity'
    data = {
        'temperature': 25,
        'weather': 'Sunny'
    }
    expected_response = {'error': 'City not found'}

    response = client.put(f'/weather/{city}', json=data)
    assert response.status_code == 404
    assert response.json == expected_response



def test_delete_weather_valid_data(client):
    city = 'London'
    expected_response = {'message': 'Weather data deleted successfully'}

    response = client.delete(f'/weather/{city}')
    assert response.status_code == 200
    assert response.json == expected_response


def test_delete_weather_invalid_data(client):
    city = 'NonexistentCity'
    expected_response = {'error': 'City not found'}

    response = client.delete(f'/weather/{city}')
    assert response.status_code == 404
    assert response.json == expected_response


