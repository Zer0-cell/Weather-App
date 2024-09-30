import requests

# Function to get weather data from OpenWeatherMap
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    # Make the API request
    response = requests.get(complete_url)
    
    # Convert response to JSON
    data = response.json()
    
    # Check if the city is found
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        
        # Extracting relevant data
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]

        # Display the weather information
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {description}")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
    else:
        print(f"City '{city}' not found.")

if __name__ == "__main__":
    # Get the API key from the user (replace with your own API key)
    api_key = "<Enter your API Key here>"
    
    # Input city name
    city = input("Enter the city name: ")
    
    # Fetch and display weather information
    get_weather(city, api_key)

# Follow the instructions in <>
