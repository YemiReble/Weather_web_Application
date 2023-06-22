#!/usr/bin/python3
"""
A Flask program that gets weather status from an api
"""


from flask import Flask, render_template, request
from flask import send_file
import requests
from api_key.key import key, remove_char, secret_key

app = Flask(__name__, static_folder='static')
app.url_map.strict_slashes = False
# Falsh Message (You will have to obtain secrete key form
# python os.urandom().hex() function)
# app.config['SECRET_KEY'] = secret_key

app.config['STATIC_URL'] = 'static/'
app.config['STATICFILES_DIRS'] = [
    'static/*'
    ]


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

    # try:
    city = location
    api_key = key
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(
        city, api_key)
    response = requests.get(url)
    data = response.json()

    # Extract the weather information
    temperature = data['main']['temp']
    description = data['weather'][0]['description']

    # Render the HTML template with the weather information
    return render_template(
        'weather_result.html',
        city=city,
        temperature=temperature,
        description=description)


@app.errorhandler(404)
def error_page(e):
    """ This function will handle the invalid request from
    the users"""
    return render_template('error_page.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
