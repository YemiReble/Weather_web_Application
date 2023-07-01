# Weather Web Application
- [x] Daily Weather Status
- [x] Location Search
- [x] Weather Reports

## Introduction
This weather app was inspired by the current weather situation. It uses the OpenWeatherMap API to display up-to-date weather information for any location in the world. The app provides current weather conditions and weather reports. 

It also includes information about the sunrise and sunset times, humidity, and visibility.

The weather app is designed to be easy to use. The main screen displays the current weather conditions for your current
location. You can also search for weather information for any other location in the world. The app's reports are
accurate and reliable in accordance to the OpenWeatherMap Data, and they are updated every hour.

The weather app is a valuable tool for anyone who wants to stay informed about the weather. It is perfect for people who plan outdoor activities, travel, or simply want to know what to expect when they leave the house.

## Features
* Easy to use interface
* Current weather conditions
* Up-to-date weather information for any location in the world
* Accurate and reliable reports in accordance to the OpenWeatherMap API Data
* Information about the **Max and Min**, **Sunrise and Sunset Times**, **Humidity**, and what the weather feels like

## How To Use This Program
Make sure that the requirements to run this program is avalable on your machine, kindly see the
[reqirements.txt](https://github.com/YemiReble/Weather_web_Application/blob/master/requirments.txt) file if you haven't
done so but if you already have all the requirements in place, you may proceed to the following steps.

This program runs on port 5000 by default, kindly ensure that port 5000 is available or you may change it to your desired port(s).

**Step 1:** Clone this Repository
```Bash
$ git clone https://github.com/yemireble/Weather_web_Application.git
```

**Setp 2:** Change dir and run the server automatically 
```
$ cd Weather_web_Application/

Auto Run Server
$ ./auto_start_server.sh
```
**Sept 3:** Now that the server is running, head over to your browser
```
http://127.0.0.1:5000
```
Your browser should display the Weather Application Home Page as shown below
###### If You Encounter An Error
Insert your OpenWeatherMap API Key in the required file on line (8)
```
$ vim api_key/key.py
```

## User Interface Display
##### Search Section
![The Search Area](https://github.com/YemiReble/Weather_web_Application/blob/master/weather_web_flask/static/img/Search_Area.JPG)

#### Current Weather Section
![Current Weater](https://github.com/YemiReble/Weather_web_Application/blob/master/weather_web_flask/static/img/Current_weather_display.JPG)

##### Report Section
![Report Section](https://github.com/YemiReble/Weather_web_Application/blob/master/weather_web_flask/static/img/Weather_Reports.JPG)

##### Full page View
![Full Page View](https://github.com/YemiReble/Weather_web_Application/blob/master/weather_web_flask/static/img/Full_Home_Page.JPG)

