import csv

with open('names.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("%s %s"%(row['first_name'],row['last_name']))
    print(type(reader))

