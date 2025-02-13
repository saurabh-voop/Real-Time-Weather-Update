import streamlit as st
import requests

# Function to get weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    return response.json()

# Streamlit app
def main():
    st.title("Real-Time Weather Updates")
    
    api_key = st.text_input("Enter your OpenWeatherMap API Key")
    city = st.text_input("Enter city name")
    
    if st.button("Get Weather"):
        if api_key and city:
            weather_data = get_weather(city, api_key)
            if weather_data["cod"] != "404":
                if "main" in weather_data and "wind" in weather_data and "weather" in weather_data:
                    main_weather = weather_data["main"]
                    wind = weather_data["wind"]
                    weather_desc = weather_data["weather"][0]["description"]
                    
                    st.write(f"**City:** {city}")
                    st.write(f"**Temperature:** {main_weather['temp']}°C")
                    st.write(f"**Humidity:** {main_weather['humidity']}%")
                    st.write(f"**Pressure:** {main_weather['pressure']} hPa")
                    st.write(f"**Weather Description:** {weather_desc.capitalize()}")
                    st.write(f"**Wind Speed:** {wind['speed']} m/s")
                else:
                    st.error("Incomplete weather data received from the API.")
            else:
                st.error("City Not Found!")
        else:
            st.error("Please enter both API Key and City name")

if __name__ == "__main__":
    main()