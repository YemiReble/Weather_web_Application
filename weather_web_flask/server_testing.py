#!/usr/bin/python3
"""
A Flask program that gets weather status from an api
"""


from flask import Flask, render_template, request
import requests
from api_key.key import key, remove_char

app = Flask(__name__)
app.url_map.strict_slashes = False
# Falsh Message (You will have to obtain secrete key form
# python os.urandom().hex() function)
# app.config['SECRET_KEY'] = 'your secret key'

@app.route('/')
def index():
    return render_template('weather.html')

@app.route('/test/')
def server_test():
    return 'Your Application Server is working fine'

@app.route('/search/<string>', methods=['GET', 'POST'])
def search(string):
    try:
        city = string
        api_key = key
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(
            city, api_key)
        response = requests.get(url)
        data = response.json()

        # Extract the weather information
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        # Render the HTML template with the weather information
        return render_template('index.html', city=city,
            temperature=temperature, description=description)

    except Exception as e:
        return render_template('error_page.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
