import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class SerPlot:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.data = None
    
    def load_data(self):
        try:
            self.data = pd.read_csv(self.csv_file_path)
            print(f"Loaded data from '{self.csv_file_path}'")
        except FileNotFoundError:
            print(f"File not found: '{self.csv_file_path}'")
            
    def get_headers(self):
        if self.data is not None:
            return self.data.columns.tolist()
        else:
            return []

    def get_data_dict(self):
        if self.data is not None:
            return self.data.to_dict()
        else:
            return {}

    def plot_data(self, num_figures, num_axes, columns_sets_to_plot, x_axis_param):
        if self.data is None:
            print("No data loaded. Use load_data() to load data first.")
            return
        
        if num_figures * num_axes < len(columns_sets_to_plot):
            print("Insufficient number of figures and axes for the given column sets.")
            return
        
        time_data = self.data[x_axis_param]                 # Set which column should be the x axis for all plots (time)
        fig, axes = plt.subplots(num_figures, num_axes, figsize=(15, 10))     # Create the figure and axes tuples

        # Handles the case in which there is only 1 figure and 1 axis
        if num_figures == 1 and num_axes == 1:
            axes = np.array([[axes]])       # convert from tuple to array list
        elif num_figures == 1 or num_axes == 1:
            axes = axes.reshape(num_figures, num_axes)
        
        # using enumerate to create an index to columns relationship for easy iteration/plot
        for i, columns_to_plot in enumerate(columns_sets_to_plot):    # Iterate through each set of columns to plot on the same axis
            ax = axes[i // num_axes, i % num_axes]
            
            for column in columns_to_plot:     # For each column in the set, plot on the current axis
                ax.plot(time_data, self.data[column],'o-',linewidth = .1, label=column)
            
            ax.set_xlabel(x_axis_param)
            ax.set_ylabel(", ".join(columns_to_plot))
            ax.set_title(f"{', '.join(columns_to_plot)} vs. {x_axis_param}")
            ax.legend()

        plt.tight_layout()
        plt.show()

        

                  

if __name__ == "__main__":
    num_figures = 2
    num_axes = 1
    columns_to_plot = ['roll', 'pitch', 'yaw', 'gx','gy','yaw']
    col_sets_to_plot = [['x','y','vx','vy'],['z','tm']]
    x_axis_param = 'time'
    serial_plot = SerPlot('XY_SR_003.csv')

    serial_plot.load_data()

    headers = serial_plot.get_headers()
    print(f"CSV Headers: {headers}")

    data_dict = serial_plot.get_data_dict()
    
    serial_plot.plot_data(num_figures,num_axes, col_sets_to_plot, x_axis_param)
