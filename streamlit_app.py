# Liam DiFalco - CSI-260
# This assignment was built using the help of AI
# ChatGPT was used to create a the graph of provided data during this first phase
# The rest of this code was built using resources from Kaggle.../https://www.kaggle.com/code/alexisbcook/line-charts

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the Dataset
data = pd.read_csv('/kaggle/input/every-porsche-911/porsche_911.csv')

# Display the first few rows to understand the structure of the data
data.head()

missing_values = data.isnull().sum()
print("Missing values:\n", missing_values)

summary_statistics = data.describe()
print("Summary Statistics:\n", summary_statistics)


#Docstring by Liam DiFalco
#Start ChatGPT Section... "write me code for Kaggle to make a histogram for Maximum Speed and Start of Production"
# Create basic graph
plt.hist(data['start_of_production'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Start of Production')
plt.ylabel('Maximum Speed (km/h)')
plt.title('Maximum Speed Distribution by Start of Production Year')
plt.grid(True)
plt.show()
#End ChatGPT Section
#Docstrings by Liam DiFalco

Acceleration = data['acceleration_0-60mph']
Year = data['start_of_production']
plt.scatter(Year, Acceleration, color='skyblue', marker='.')
# Average line
average_acceleration = Acceleration.groupby(Year).mean()
plt.plot(average_acceleration.index, average_acceleration.values, color='orange', label='Average Acceleration', linewidth=2)
plt.title('Acceleration Over time', fontsize=14)
plt.xlabel('acceleration_0-60mph', fontsize=8)
plt.ylabel('year', fontsize=8)
plt.grid(True)
plt.show()
# Create a line plot
#plt.plot(Year, Acceleration)
Power = data['power']
Year = data['start_of_production']
plt.scatter(Year, Power, color='skyblue', marker='.')
# Average line
#average_acceleration = Acceleration.groupby(Power).mean()
#plt.plot(average_acceleration.index, average_acceleration.values, color='orange', label='Average HorsePower', linewidth=2)
plt.title('Horse Power Over time', fontsize=14)
plt.xlabel('Year', fontsize=8)
plt.ylabel('Horsepower', fontsize=8)
plt.grid(True)
plt.show()
# Create a line plot
#plt.plot(Year, Acceleration)
