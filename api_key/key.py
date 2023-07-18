#!/usr/bin/python3
""" My Openweathermap API """


import datetime

# Insert you API key here
key = ""

# Secret key for flash message
secret_key = '3346dcf0af8ed02e7a0dedf29db000a630a5aede7922ecc9'

# Some other key list to use
other_keys = [{'fb64d30a9e2586b13b979e4d9d67fa16999c29f5251593cb'},
              {'3fe8093cad2236adee3fac7335f38ad2b58b1c9ef84e77ae'},
              {'52e14ea0a598ff5459769a0754c3ece54ff8514620d2ced6'}]


def remove_char(char):
    """ Function that remove unwanted characters "?q="
    from the string given by the user"""
    # char = request.form['char']
    result = char.replace('?q=', '')
    return (result)


def kelvin_to_degree(temp):
    """This function convert Temprature from 'kelvin to Celsius'"""
    kelvin = 273.15
    degree = temp - kelvin
    return round(degree)


def format_date(d):
    d = str(d)
    if len(d) == 1:
        return "0" + d
    else:
        return d


def convert_time(timezone, rise_set):
    """Function that convert UTC Time Stamp"""
    time = datetime.datetime.utcfromtimestamp(rise_set).timestamp() + timezone
    time = datetime.datetime.fromtimestamp(time).strftime('%I:%M')
    return time


def convert_time_old(time):  # This function doesn't work as expected
    """Function that convert API time time"""
    seconds_to_sunrise = time
    date_e = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=seconds_to_sunrise)
    return format_date(date_e.strftime("%I:%M"))
