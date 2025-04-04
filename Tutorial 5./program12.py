import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('weather.csv')

# 1. Print first 10 rows of weather data
print(df.head(10))

# 2. Find the maximum and minimum temperature
max_temp = df['temperature'].max()
min_temp = df['temperature'].min()
print(f"Maximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")

# 3. List the places with temperature less than 28°C
places_below_28 = df[df['temperature'] < 28]['place']
print("Places with temperature less than 28°C:")
print(places_below_28)

# 4. List the places with weather = "Cloudy"
places_cloudy = df[df['weather'] == 'Cloudy']['place']
print("Places with weather = 'Cloudy':")
print(places_cloudy)

# 5. Sort and display each weather and its frequency
weather_frequency = df['weather'].value_counts()
print("Weather Frequency:")
print(weather_frequency)

# 6. Create a bar plot to visualize temperature of each day
plt.figure(figsize=(10,6))
plt.bar(df['date'], df['temperature'], color='skyblue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature of Each Day')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
