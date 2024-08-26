# Weather Dashboard MVP

This is a simple Weather Dashboard application that provides real-time weather information for a specified city using the OpenWeatherMap API. The application is built with Flask and Python.

## Features

- Get current weather information including temperature, humidity, wind speed, and weather description.
- Simple and user-friendly interface.
- Error handling for invalid city names or API issues.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or later
- Pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Mark-Finley/weather-dashboard-mvp.git
   cd weather-dashboard-mvp
   ```
2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  
    # On Windows: venv\Scripts\activate
    ```
3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Run the Flask application:**
    ```bash
    python app.py
    ```
2. **Access the application:**

    Open your web browser and go to http://127.0.0.1:5000.

3. **Enter a city name:**

    The weather information for the specified city will be displayed.

**Example**

- City: "New York"
- Weather Info: "Clear, Temperature: 25°C, Humidity: 60%, Wind Speed: 5 m/s"

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.