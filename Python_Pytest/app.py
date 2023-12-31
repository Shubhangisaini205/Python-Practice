from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route('/weather/<string:city>', methods=["GET"])
def Display_Weather(city):
    if city in weather_data:
        return jsonify(weather_data[city]),200
    else:
        return jsonify({'error': 'City not found'}), 400
    

@app.route('/weather', methods=["POST"])
def Post_weather():
    data = request.get_json()
    city = data.get('city')
    temperature = data.get('temperature')
    weather = data.get('weather')
    if city is None or temperature is None or weather is None:
        return jsonify({'error': 'Invalid data'}), 400
    else:
        weather_data[city] = {'temperature': temperature, 'weather': weather}
        return jsonify({'message': 'Weather data added successfully'})

@app.route('/weather/<string:city>', methods=["PUT"])
def UpDate_weather(city):
    if city not in weather_data:
        return jsonify({'error': 'City not found'}), 404

    data = request.get_json()
    temperature = data.get('temperature')
    weather = data.get('weather')

    if temperature is not None:
        weather_data[city]['temperature'] = temperature
    if weather is not None:
        weather_data[city]['weather'] = weather

    return jsonify({'message': 'Weather data updated!!!'})

@app.route('/weather/<string:city>', methods=["DELETE"])
def Delete_Weather(city):
    if city in weather_data:
        del weather_data[city]
        return jsonify({'message': 'Weather data deleted successfully'})
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
