import os
import csv
##### Counts the rows
path = os.path.join("..", "Resources", "budget_data.csv")

with open(path) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader)
    data = list(csvreader)
    row_count = len(data)
    print(row_count)

#### Index
c1 = []
c2 = []
with open(path) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        c1.append(row[0])
        c2.append(row[1])
    # print(row[0] + "is rated " + row[1])
for ind, date1 in enumerate(c2):
    print(f"[{ind} {date1}")
# for x in range(len(c2)):
#     print(c2[x])
