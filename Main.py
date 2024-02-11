import requests
import configparser
from flask import Flask, render_template, request
import wikipedia 

app = Flask(__name__)

@app.route('/')
def dashboard():
	return render_template('home.html')

@app.route('/results', methods=['POST'])
def render_results():
    zip_code = request.form['zipCode']
    api_key = get_api_key()
    data = get_weather_results(zip_code, api_key)
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    pressure = "{0:.2f}".format(data["main"]["pressure"])
    humidity = "{0:.2f}".format(data["main"]["humidity"])
    weather = data["weather"][0]["main"]
    location = data["name"]
    info = wikipedia.summary(location + "City India",sentences = 3)

    return render_template('results.html',location=location, temp=temp,feels_like=feels_like,
     weather=weather,info=info,pressure= pressure,humidity=humidity)

def get_api_key():
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config['openweathermap']['api']

def get_weather_results(zip_code, api_key):
	api_url =("http://api.weatherapi.com/v1/current.json?key=5039835f31a64d089cc71051241102&q=London&aqi=no")
	r = requests.get(api_url)
	return r.json()



if __name__ == '__main__':
	app.debug = True
	app.run()


