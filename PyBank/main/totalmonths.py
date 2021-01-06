import os
import csv

path = os.path.join("..", "Resources", "budget_data.csv")

with open(path) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader)
    data = list(csvreader)
    row_count = len(data)
    print(f"Total Months: {row_count}")