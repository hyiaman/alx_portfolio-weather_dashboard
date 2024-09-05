from app import get_weather_and_forecast

# Dependencies:
# pip install pytest-mock
# import pytest


class TestGetWeatherAndForecast:
    # Returns current weather and hourly forecast for valid city name
    def test_returns_current_weather_and_hourly_forecast_for_valid_city_name(self, mocker):
        city_name = "London"
        mock_weather_response = {
            'name': 'London',
            'main': {'temp': 15},
            'weather': [{'description': 'clear sky', 'icon': '01d'}]
        }
        mock_forecast_response = {
            'list': [
                {'dt_txt': '2023-10-01 12:00:00', 'main': {'temp': 16}, 'weather': [
                    {'description': 'few clouds', 'icon': '02d'}]},
                {'dt_txt': '2023-10-01 15:00:00', 'main': {'temp': 17}, 'weather': [
                    {'description': 'scattered clouds', 'icon': '03d'}]}
            ]
        }
    
        mocker.patch('requests.get', side_effect=[
            mocker.Mock(status_code=200, json=lambda: mock_weather_response),
            mocker.Mock(status_code=200, json=lambda: mock_forecast_response)
        ])
    
        current_weather, hourly_forecast = get_weather_and_forecast(city_name)
    
        assert current_weather == {
            'city': 'London',
            'temperature': 15,
            'description': 'clear sky',
            'icon': '01d'
        }
        assert hourly_forecast == [
            {'time': '2023-10-01 12:00:00', 'temperature': 16, 'description': 'few clouds', 'icon': '02d'}
        ]

    # Handles invalid city names gracefully
    def test_handles_invalid_city_names_gracefully(self, mocker):
        city_name = "InvalidCity"
    
        mocker.patch('requests.get', side_effect=[
            mocker.Mock(status_code=404),
            mocker.Mock(status_code=404)
        ])
    
        current_weather, hourly_forecast = get_weather_and_forecast(city_name)
    
        assert current_weather is None
        assert hourly_forecast is None
