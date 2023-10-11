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

    def plot_data(self, num_figures, num_axes, columns_to_plot, x_axis_param):
        if self.data is None:
            print("No data loaded. Use load_data() to load data first.")
            return
        if num_figures * num_axes < len(columns_to_plot):
            print("Insufficient number of figures and axes to plot all selected columns.")
            return
        
        time_data = self.data[x_axis_param]                 # set which column should be the x axis for all plots (time)
        fig, axes = plt.subplots(num_figures, num_axes, figsize=(15, 5))     # create the figure and axes tuples

        # instead of writing multiple instances of ax.plot, we can use the
        # enumerate function to run the loop through per eac columns_to_plot
        for i, column in enumerate(columns_to_plot):    # match up an iterated index with each column_to_plot
            ax = axes[i // num_axes, i % num_axes]      # iterate through each plot with a rolling buffer style calc
            ax.plot(time_data, self.data[column], label=column)
            ax.set_xlabel(x_axis_param)
            ax.set_ylabel(column)
            ax.set_title(f"{column} vs. {x_axis_param}")
            ax.legend()

        plt.tight_layout()
        plt.show()
        

                  

# if __name__ == "__main__":
#     num_figures = 2
#     num_axes = 3
#     columns_to_plot = ['roll', 'pitch', 'yaw', 'gx','gy','yaw']
#     x_axis_param = 'time'
#     serial_plot = SerPlot('XY_SR_003.csv')

#     serial_plot.load_data()

#     headers = serial_plot.get_headers()
#     print(f"CSV Headers: {headers}")

#     data_dict = serial_plot.get_data_dict()
    
#     serial_plot.plot_data(num_figures,num_axes, columns_to_plot, x_axis_param)
