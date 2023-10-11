import serial
import csv

stop_flag = True

# Define the serial port settings
serial_port = '/dev/tty.usbmodem141859801'  # Replace with your serial port name
baud_rate = 115200  # Adjust the baud rate as per your device's settings

# Define the file to save data to
csv_filename = 'data.csv'

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)

# Create a CSV file and a CSV writer
csv_file = open(csv_filename, mode='w', newline='')
csv_writer = csv.writer(csv_file)

# Initialize a buffer to store received data
data_buffer = []

# a precondition check to detect the start sequence of 3 stars
while True:
    pre_data = ser.readline().decode('utf-8').strip()
    if pre_data == '***':
        print('detected stars')
        break

try:
    while True:
        # Read data from the serial port
        data = ser.readline().decode('utf-8').strip()

        # Append data to the buffer
        data_buffer.append(data)
        
        # Check if "****" is in the received data
        if data == 'Now in wait mode...':
            # Close the CSV file
            print('close serial port')
            # stop_flag = False
            break
        else:
            # Start writing data to the CSV file
            print(data_buffer)
            for line in data_buffer:
                csv_writer.writerow([line])

        # Clear the buffer for the next set of data
        data_buffer.clear()

finally:
    # Close the serial port
    ser.close()
