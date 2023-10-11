import serial
import csv
import os

serial_port = '/dev/tty.usbmodem141859801'  # Replace with your serial port name
baud_rate = 115200  # Adjust the baud rate as per your device's settings
# Serial port configuration
ser = serial.Serial(serial_port, baud_rate)  # Replace 'COM1' with your serial port name
keyword_start = "testing begin..."
keyword_end = "testing done..."

# Find the next CSV file number
existing_files = [f for f in os.listdir() if f.startswith("XY_SR_") and f.endswith(".csv")]
next_file_number = len(existing_files) + 1
csv_filename = f"XY_SR_{next_file_number:03d}.csv"

# Initialize CSV file and writer
with open(csv_filename, 'w', newline='\n') as csv_file:
    csv_writer = csv.writer(csv_file, quotechar="'")

    # Wait for the "testing begin..." keyword
    while True:
        line = ser.readline().decode("utf-8").strip('\r\n')
        if line == keyword_start:
            break

    # Write data to the CSV file until "testing done..." is received
    while True:
        line = ser.readline().decode("utf-8").strip('\r\n')
        print(line)
        if line == keyword_end:
            break
        elif "nan" not in line:
            # Split the received data into CSV columns if needed
            # For example, if data is comma-separated:
            csv_row = line.strip('"').split(',')
            
            # Write the row to the CSV file
            csv_writer.writerow(csv_row)

print(f"CSV file '{csv_filename}' created and saved.")
