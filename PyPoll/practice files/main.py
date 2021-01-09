import os
import csv

path = os.path.join("..", "Resources", "election_data.csv")

with open(path) as electionfile:
    csvreader = csv.reader(electionfile, delimiter=",")
    csv_header = next(csvreader)
    data = list(csvreader)
    row_count = len(data)
    print(f"Total Votes: {row_count}")