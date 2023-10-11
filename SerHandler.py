import os
import serial
import csv

class SerHandler:
    def __init__(self, port, baud_rate, start_keyword, end_keyword):
        self.port = port
        self.baud_rate = baud_rate
        self.start_keyword = start_keyword
        self.end_keyword = end_keyword
        self.serial = None
        self.serial_is_connected = False
        self.csv_file = None
        self.is_recording = False
        self.csv_filename = None 
        self.csv_writer = None
    
    # This method simply attempts to connect to the serial port and handles any exceptions
    def connect_serial(self):
        try:
            self.serial = serial.Serial(self.port, self.baud_rate)          # create the serial object
            print(f"connected to {self.port}, at baud rate of {self.baud_rate}")
            self.serial_is_connected = True
        except serial.SerialException as se:
            print(f"Can't connect to port {self.port}: due to {se}")
            return False
        return True
    
    # This method checks the current directory and counts the number of data csv files
    # It then returns the filename of the next csv to be created to store new data 
    def get_next_csv_filename(self):
        # create a list of files that have the following conditions
        csv_files = [f for f in os.listdir() if f.startswith("XY_SR_") and f.endswith(".csv")]      # amazing that you can do this in 1 line
        next_file_num = len(csv_files) + 1
        self.csv_filename = f"XY_SR_{next_file_num:03}.csv"         # add leading zeros
        return self.csv_filename
    
    # This method starts saving data to the said csv file when called by creating the csv file
    # and creating a csv writer object
    def start_recording(self):
        # check that we have an established connection to the port
        if not self.serial_is_connected:
            print("Not connected to serial port")
            return 
        else:
            self.get_next_csv_filename()                                    # generate next csv filename
            self.is_recording = True
        
    # This method simply stops data collection and closes the file
    def stop_recording(self):
        self.is_recording = False

        
    # This is where the magic happens and the data is actually read from the serial port 
    # and stored into the defined csv file given conditions
    def read_data(self):
        if not self.serial_is_connected:
            print("Serial connection is not established.")
            return

        # using the with keyword, we can open and iterate on the file with 1 line
        with open(self.csv_filename, 'w', newline='\n') as csv_file:
            self.csv_writer = csv.writer(csv_file, quotechar="'")

            # Wait for the "testing begin..." keyword
            while True:
                line = self.serial.readline().decode("utf-8").strip('\r\n')
                print(line)
                if line == self.start_keyword:
                    break

            # Write data to the CSV file until "testing done..." is received
            while True:
                line = self.serial.readline().decode("utf-8").strip('\r\n')
                print(line)
                if line == self.end_keyword:
                    break
                elif "nan" not in line:     # sometimes there are nan measurements, filter those out
                    csv_row = line.strip('"').split(',')        # strip "" marks to clean up csv file 
                    self.csv_writer.writerow(csv_row)           # Write the row to the CSV file
                    
                    
# if __name__ == "__main__":
#     port_name = '/dev/tty.usbmodem141859801'  
#     baud_rate = 115200  

#     sh = SerialHandler(port_name, baud_rate, "testing begin...", "testing done...")
#     sh.connect_serial()
#     sh.start_recording()
#     if sh.is_recording:
#         sh.read_data()
#     else:
#         sh.stop_recording()
    
    