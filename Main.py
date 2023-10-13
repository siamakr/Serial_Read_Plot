import time
import numpy as np
from SerHandler import SerHandler
from SerPlot import SerPlot

if __name__ == "__main__":
    port_name = '/dev/tty.usbmodem141859801'  
    baud_rate = 115200  
    csv_basename = "XY_SR_"
    num_figures = 2
    num_axes = 3
    columns_to_plot = ['roll', 'pitch', 'yaw', 'gx','gy','yaw']
    x_axis_param = 'time'

    sh = SerHandler(port_name, baud_rate, "testing begin...", "testing done...", csv_basename)
    sh.connect_serial()
    sh.start_recording()
    if sh.is_recording:
        sh.read_data()
    else:
        sh.stop_recording()


    serial_plot = SerPlot(sh.csv_filename)

    serial_plot.load_data()

    headers = serial_plot.get_headers()
    print(f"CSV Headers: {headers}")

    data_dict = serial_plot.get_data_dict()
    
    serial_plot.plot_data(num_figures,num_axes, columns_to_plot, x_axis_param)