#!/usr/bin/python3
"""
A Flask program that gets weather status from an api
"""


from flask import Flask, render_template, request
from flask import send_file
import requests
import datetime
from api_key.key import key, kelvin_to_degree, secret_key
from api_key.key import convert_time

app = Flask(__name__, static_folder='static')
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return render_template('weather.html')


@app.route('/test/')
def server_test():
    """ Just for testing if the server is running"""
    return 'Your Application Server is working fine'


@app.route('/search/', methods=['GET', 'POST'])
def search():
    """This function processes the request sent my the user"""
    location = request.args.get('q')

    try:
        city = location
        api_key = key
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(
            city, api_key)
        response = requests.get(url)
        data = response.json()

        # Extract the weather information
        kelvin_temperature = data['main']['temp']
        description = data['weather'][0]['description']
        kelvin_feels_like = data['main']['feels_like']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        pressure = data['main']['pressure']
        sunrises = data['sys']['sunrise']
        sunsets = data['sys']['sunset']
        humidity = data['main']['humidity']
        country = data['sys']['country']
        time_zone = data['timezone']

        # Convert Temperature
        temperature = kelvin_to_degree(kelvin_temperature)
        feels_like = kelvin_to_degree(kelvin_feels_like)
        min_temp = kelvin_to_degree(temp_min)
        max_temp = kelvin_to_degree(temp_max)

        # Time conversion
        sunrise = convert_time(time_zone, sunrises)
        sunset = convert_time(time_zone, sunsets)

        # Render the HTML template with the weather information
        return render_template(
            'weather_result.html',
            city=city,
            temperature=temperature,
            description=description,
            feels_like=feels_like,
            min_temp=min_temp,
            max_temp=max_temp,
            humidity=humidity,
            country=country,
            sunrise=sunrise,
            sunset=sunset,
            pressure=pressure)

    # Raise Exception when user enter an invalid city or country name
    except KeyError:
        return render_template('key_error.html', city=city)
    # Raise Exception when Webserver lost connection to the API
    # except ConnectionError:
    #    return render_template('connection_error.html')


@app.errorhandler(404)
def error_page(e):
    """ This function will handle the invalid request from
    the users"""
    return render_template('error_page.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
