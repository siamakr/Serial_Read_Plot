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

# Create the initial plot
fig1, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize = (25,10))
fig2, ((ax5, ax6), (ax7, ax8)) = plt.subplots(2,2, figsize = (25,10))

# Initialize empty lists
print(skipped_items)
print(lst)

# append each new row of data to their corresponding key/value pair in dictionary lst
data_dict = {}
for column in headers:
    data_dict[column] = data[column].tolist()

        # customize each plot and their corresponding data sets
# Update the first subplot (X and Y data)
ax1.plot(data_dict['x'], data_dict['y'])
ax1.set_title('X vs. Y')

# Update the second subplot (Vx and Vy data)

ax2.plot(data_dict['time'], data_dict['vx'])
ax2.set_title('Vx and Vy')


ax3.plot( data_dict['time'],data_dict['roll'])
# ax3.plot(data_dict['time'],data_dict['upos0'], 'go-', lw=1)
ax3.plot(data_dict['time'],data_dict['yaw'], 'bo-', lw=1)
ax3.set_title('Roll/Roll SP')


ax4.plot(data_dict['time'],data_dict['pitch'], 'c')
# ax4.plot(data_dict['time'],data_dict['upos1'], 'ro-', lw=1)
ax4.plot(data_dict['time'],data_dict['tm'], 'y')
ax4.set_title('Pitch/Pitch SP')

    # Update the first subplot (X and Y data)

ax5.plot(data_dict['x'], data_dict['y'], 'bo-', lw=1)
ax5.set_title('gx and gy')

# Update the second subplot (Vx and Vy data)

ax6.plot( data_dict['time'],data_dict['u0'], 'ro-', lw=1)
# ax3.plot(data_dict['time'],data_dict['upos0'], 'go-', lw=1)
ax6.plot(data_dict['time'],data_dict['gx'], 'bo-', lw=1)
ax6.set_title('u0 and gx')


ax7.plot( data_dict['time'],data_dict['u1'], 'ro-', lw=1)
# ax3.plot(data_dict['time'],data_dict['upos0'], 'go-', lw=1)
ax7.plot(data_dict['time'],data_dict['gy'], 'bo-', lw=1)
ax7.set_title('u1 and gy')

# ax8.clear()
# ax8.plot(data_dict['time'],data_dict['tm'], 'co-', lw=1)
# # ax4.plot(data_dict['time'],data_dict['upos1'], 'ro-', lw=1)
# ax8.plot(data_dict['time'],data_dict['u1'], 'yo-', lw=1)
# ax8.set_title('Pitch/Pitch SP')


# Show the animation
plt.tight_layout()
plt.show()

