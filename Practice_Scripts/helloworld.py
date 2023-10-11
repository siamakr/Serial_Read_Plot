import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import time

# Function to read one row of data from the CSV file
    # Read one row of data from the CSV file
data = pd.read_csv("XY_SR_001.csv")
xdata = data['X']
ydata = data['Y']
vxdata = data['Vx']
vydata = data['Vy']

# Function to update the plot
def update(frame):
    # Read one row of data from the CSV file

    # Append the data to the existing plot
    # Append the data to the existing plots
    x_data.append(data['X'][frame])
    y_data.append(ydata[frame])
    vx_data.append(frame)  # Assuming "Vx" is the 2nd column
    vy_data.append(vydata[frame])  # Assuming "Vy" is the 6th column
    
    if len(vx_data) > 50:
        vx_data.pop(0)
        vy_data.pop(0)
    
    # Update the first subplot (X and Y data)
    ax1.clear()
    ax1.plot(x_data, y_data, 'bo-', lw=2)
    ax1.set_title('X vs. Y')
    
    # Update the second subplot (Vx and Vy data)
    ax2.clear()
    ax2.plot(vx_data, vy_data, 'ro-', lw=2)
    ax2.set_title('Vx vs. Vy')
    
    return ax1, ax2

# Initialize empty lists for x and y data
x_data = []
y_data = []
vy_data = []
vx_data = []

# Create the initial plot
fig, (ax1, ax2) = plt.subplots(2,1)

# Create the animation
ani = FuncAnimation(fig, update, frames=20000, interval=1)  # Update every 1000 milliseconds (1 second)

# Show the animation
plt.show()
