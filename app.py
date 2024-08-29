from flask import Flask, render_template, request, redirect, flash, url_for, session
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Add your OpenWeatherMap API Key here
API_KEY = os.getenv('WEATHER_API_KEY')

# Function to get current weather and 3-hour forecast


def get_weather_and_forecast(city_name):
    # URLs for OpenWeatherMap API endpoints
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric"
    
    # Fetch data from APIs
    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)
    
    if weather_response.status_code == 200 and forecast_response.status_code == 200:
        weather_data = weather_response.json()
        forecast_data = forecast_response.json()

        # Extract current weather data
        current_weather = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon']
        }

        # Extract hourly forecast data for the current day
        hourly_forecast = []
        for forecast in forecast_data['list']:
            if '12:00:00' in forecast['dt_txt']:
                hourly_forecast.append({
                    'time': forecast['dt_txt'],
                    'temperature': forecast['main']['temp'],
                    'description': forecast['weather'][0]['description'],
                    'icon': forecast['weather'][0]['icon']
                })

        return current_weather, hourly_forecast

    return None, None


@app.route('/', methods=['GET', 'POST'])
def index():
    current_weather = None
    hourly_forecast = []

    if request.method == 'POST':
        city_name = request.form.get('city')

        # Save the city name in session for reuse
        session['city_name'] = city_name

        # Get weather and forecast data
        current_weather, hourly_forecast = get_weather_and_forecast(city_name)
        if current_weather:
            flash(f"Weather data for {city_name} retrieved successfully!", 'success')
        else:
            flash(f"Could not retrieve weather data for {city_name}. Please try again.", 'error')

    return render_template('index.html', current_weather=current_weather, hourly_forecast=hourly_forecast)


@app.route('/forecast', methods=['GET'])
def five_days_forecast():
    # Retrieve the last used city from the session
    city_name = session.get('city_name', 'default_city')

    # URL for OpenWeatherMap 5-day forecast
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric"
    forecast_response = requests.get(forecast_url)

    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()

        # Extract 5-day forecast data
        five_day_forecast = []
        for forecast in forecast_data['list']:
            if '12:00:00' in forecast['dt_txt']:  # Select midday forecasts
                five_day_forecast.append({
                    'date': forecast['dt_txt'].split()[0],
                    'temperature': forecast['main']['temp'],
                    'description': forecast['weather'][0]['description'],
                    'icon': forecast['weather'][0]['icon']
                })

        return render_template('forecast.html', forecast=five_day_forecast)
    else:
        flash(f"Could not retrieve 5-day forecast data for {city_name}.", 'error')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=False)
