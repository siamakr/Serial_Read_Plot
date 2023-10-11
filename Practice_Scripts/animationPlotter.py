import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import time

# Function to read one row of data from the CSV file
# Read one row of data from the CSV file
data = pd.read_csv("XY_SR_012.csv")
headers = data.columns.tolist()

# create a dictionary to store the empty lists for each header/column frame
lst = {header: [] for header in headers}
# create a set of dictionary items that aren't a moving frame
skipped_items = set(['x','y'])


# Initialize empty lists
print(skipped_items)
print(lst)
# Function to update the plot
def update_fig_1(frame):
    # append each new row of data to their corresponding key/value pair in dictionary lst
    for key in lst:
        lst[key].append(data[key][frame])

    # pop the last element in the list dictionary, except if they are in the 
    # skipped items list 
    if len(lst['vx']) > 35:
        for key in lst:
            if key not in skipped_items:
                lst[key].pop(0)

    # customize each plot and their corresponding data sets
    # Update the first subplot (X and Y data)
    ax1.clear()
    ax1.plot(lst['x'], lst['y'])
    ax1.set_title('X vs. Y')
    
    # Update the second subplot (Vx and Vy data)
    ax2.clear()
    ax2.plot(lst['time'], lst['vx'])
    ax2.set_title('Vx vs. Vy')
    
    ax3.clear()
    ax3.plot( lst['time'],lst['roll'])
    # ax3.plot(lst['time'],lst['upos0'], 'go-', lw=1)
    ax3.plot(lst['time'],lst['u0'], 'bo-', lw=1)
    ax3.set_title('Roll/Roll SP')

    ax4.clear()
    ax4.plot(lst['time'],lst['pitch'], 'c')
    # ax4.plot(lst['time'],lst['upos1'], 'ro-', lw=1)
    ax4.plot(lst['time'],lst['u1'], 'y')
    ax4.set_title('Pitch/Pitch SP')
    
    
    
    return ax1, ax2, ax3, ax4
def update_fig_2(frame):

    # the data reading from csv is handled by update_fig_1
    
    # Update the first subplot (X and Y data)
    ax5.clear()
    ax5.plot(lst['x'], lst['y'], 'bo-', lw=1)
    ax5.set_title('X vs. Y')
    
    # Update the second subplot (Vx and Vy data)
    ax6.clear()
    ax6.plot(lst['time'], lst['vx'], 'ro-', lw=1)
    ax6.set_title('Vx vs. Vy')
    
    ax7.clear()
    ax7.plot( lst['time'],lst['z'], 'ro-', lw=1)
    # ax3.plot(lst['time'],lst['upos0'], 'go-', lw=1)
    ax7.plot(lst['time'],lst['vz'], 'bo-', lw=1)
    ax7.set_title('Z and Vz')

    ax8.clear()
    ax8.plot(lst['time'],lst['tm'], 'co-', lw=1)
    # ax4.plot(lst['time'],lst['upos1'], 'ro-', lw=1)
    ax8.plot(lst['time'],lst['u1'], 'yo-', lw=1)
    ax8.set_title('Pitch/Pitch SP')
    
    
    
    return ax5, ax6, ax7, ax8


# Create the initial plot
fig1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize = (15,10))
fig2, ((ax5, ax6), (ax7, ax8)) = plt.subplots(2,2, figsize = (15,10))


# Create the animation
ani_1 = FuncAnimation(fig1, update_fig_1, frames=len(data), interval=10)  
ani_2 = FuncAnimation(fig2, update_fig_2, frames=len(data), interval=10)  

# Show the animation
plt.tight_layout()
plt.show()
