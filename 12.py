import csv
def read_whitelist(whitelist_file):
    whitelist = set()
    with open(whitelist_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            whitelist.add(row[0])  # Assuming IP addresses are in the first column
    return whitelist

whitelist_file = 'whitelist.csv'
whitelist = read_whitelist(whitelist_file)
print(whitelist)
