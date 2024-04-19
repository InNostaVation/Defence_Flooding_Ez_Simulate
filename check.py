import csv
import re
from collections import defaultdict
from datetime import datetime

# Define a function to parse the log file and extract required information
def parse_log_file(log_file):
    # Create a defaultdict to store IP related information
    ip_info = defaultdict(list)
    
    # Regular expression pattern to extract IP address and timestamp
    pattern = r'(\d+\.\d+\.\d+\.\d+) .*?\[(\d+/\w+/\d+:\d+:\d+:\d+ \+\d+)\]'

    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                ip_address = match.group(1)
                timestamp_str = match.group(2)
                timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')
                ip_info[ip_address].append(timestamp)
    return ip_info

# Function to write blacklisted IPs into a CSV file
def write_to_csv(blacklist, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Blacklisted IPs'])
        writer.writerows([[ip] for ip in blacklist])
        
# Function to read IPs from whitelist CSV file
def read_whitelist(whitelist_file):
    whitelist = set()
    with open(whitelist_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            whitelist.add(row[0])  # Assuming IP addresses are in the first column
    return whitelist

# Main function
def main():
    log_file = 'logs.txt'
    whitelist_file = 'whitelist.csv'
    blacklist_file = 'blacklist.csv'

    ip_info = parse_log_file(log_file)
    whitelist = read_whitelist(whitelist_file)
    # Create blacklist for IPs with high request frequency
    blacklist = set()
    for ip, timestamps in ip_info.items():
        # Check if IP is in whitelist
        if ip not in whitelist:
            # Define a time window (e.g., 1 minute)
            window_start = timestamps[0]
            for i in range(len(timestamps)):
                window_end = timestamps[i]
                count = sum(1 for t in timestamps if window_start <= t <= window_end)
                if count > 100:  # Modify threshold as needed
                    blacklist.add(ip)
                    break
                window_start = times./tamps[i]
            
    #blacklist = parse_log_file(log_file)
    write_to_csv(blacklist, blacklist_file)

if __name__ == "__main__":
    main()

