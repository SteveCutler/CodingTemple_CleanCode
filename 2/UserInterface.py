from DataParser import DataParser
from weather_data import WeatherDataFetcher

class UserInterface:
    DataParser = DataParser()
    

    def __init__(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = WeatherDataFetcher(city, detailed)
                detailedForecast = forecast.get_detailed_forecast()
                print(detailedForecast)
            else:
                forecast = WeatherDataFetcher(city, detailed)
                basicforecast = forecast.display_weather()
                print(basicforecast)
            pass
    
        
    