import csv
from collections import defaultdict
from datetime import datetime

# Define a function to parse the log file and extract required information
def parse_log_file(log_file):
    # Create a defaultdict to store IP related information
    ip_info = defaultdict(list)

    with open(log_file, 'r') as file:
        for line in file:
            parts = line.split()

            # Extract IP address and timestamp
            ip_address = parts[0]
            timestamp_str = parts[3][1:] + ' ' + parts[4][:-1]  # Combine date and time parts
            timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')

            # Update IP info
            ip_info[ip_address].append(timestamp)

    # Calculate times_visits, start_time, and end_time for each IP
    ip_data = []
    for ip, timestamps in ip_info.items():
        times_visits = len(timestamps)
        start_time = min(timestamps)
        end_time = max(timestamps)
        ip_data.append((ip, times_visits, start_time, end_time))

    return ip_data

# Function to write extracted data into a CSV file
def write_to_csv(data, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP Address', 'Times Visited', 'Start Time', 'End Time'])
        writer.writerows(data)

# Main function
def main():
    log_file = 'logs.txt'
    csv_file = 'extracted_data.csv'

    extracted_data = parse_log_file(log_file)
    write_to_csv(extracted_data, csv_file)

if __name__ == "__main__":
    main()
