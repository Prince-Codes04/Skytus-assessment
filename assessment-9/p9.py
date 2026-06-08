import csv

file_name = input("Enter CSV file name: ")

with open(file_name, "r") as file:
    reader = csv.reader(file)

    print("\nCSV Content:")
    for row in reader:
        print("\t".join(row))