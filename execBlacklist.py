import csv
import subprocess

def add_to_blacklist(ip_address):
    subprocess.run(["docker", "exec", "victim", "iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"])

def read_blacklist_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            ip_address = row[0].strip()
            #print(ip_address)
            add_to_blacklist(ip_address)

# Example usage
if __name__ == "__main__":
    blacklist_file = "blacklist.csv"
    read_blacklist_from_csv(blacklist_file)

