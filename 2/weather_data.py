from DataParser import DataParser
class WeatherDataFetcher:

    def __init__(self, city, detailed):
        self.city = city
        self.detailed = detailed

    def fetch_weather_data(city):
        print(f"Fetching weather data for {city}...")
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data.get(city, {})

    def get_detailed_forecast(self):
        # Function to provide a detailed weather forecast for a city
        data = WeatherDataFetcher.fetch_weather_data(self.city)
        return DataParser.parse_weather_data(data, self.city)
    
    def display_weather(self):
    # Function to display the basic weather forecast for a city
        data = WeatherDataFetcher.fetch_weather_data(self.city)
        if not data: 
            return f"Weather data not available for {self.city}..."
            
        else:
            weather_report = DataParser.parse_weather_data(data, self.city)
            return weather_report
