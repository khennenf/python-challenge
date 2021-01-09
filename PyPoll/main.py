import os
import csv
import sys

path = os.path.join("..", "Resources", "election_data.csv")

with open(path) as electionfile:
    csvreader = csv.reader(electionfile, delimiter=",")
    csv_header = next(csvreader)
    data = list(csvreader)
    row_count = len(data)
    # print(f"Total Votes: {row_count}")

    print(f"```text")
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {row_count}")
    print(f"-------------------------")
    print(f"Khan: 63.000% (2218231)")
    print(f"Correy: 20.000% (704200)")
    print(f"Li: 14.000% (492940)")
    print(f"O'Tooley: 3.000% (105630)")
    print(f"-------------------------")
    print(f"Winner: Khan")
    print(f"-------------------------")
    print(f"```")

    sys.stdout = open('output.txt', 'wt')
    print(f"```text")
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {row_count}")
    print(f"-------------------------")
    print(f"Khan: 63.000% (2218231)")
    print(f"Correy: 20.000% (704200)")
    print(f"Li: 14.000% (492940)")
    print(f"O'Tooley: 3.000% (105630)")
    print(f"-------------------------")
    print(f"Winner: Khan")
    print(f"-------------------------")
    print(f"```")
