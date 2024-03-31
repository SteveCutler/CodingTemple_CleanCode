class DataParser:
    # Logic for parsing weather data
    def __init__(self):
        pass

    def parse_weather_data(data, city):
        # Function to parse weather data
        if not data:
            return f"Weather data not available got {city}..."
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
