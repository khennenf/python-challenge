import os
import csv

path = os.path.join("..", "Resources", "budget_data.csv")


# Open and read csv
# c1 = []
# c2 = []
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    found = False
    amount = input("What amount are you looking for? ")
    
    
    # Read through each row of data after the header
    # for row in csv_reader:
    #     # Convert row to float and compare to grams of fiber
    #     if int(row[1]) >= 989499:
    #         print(row)
    # for row in csv_reader:
    #     if row[1] == amount:
    #         print(f"The amount is {row}")
    #This gives you the total of the whole column:
    
    total = 0
    for row in csv_reader:
        total += int(row[1])
    print(f"Total: ${total}")

    print(total)