import os
from collections import OrderedDict
import math
import csv
##### Counts the rows
path = os.path.join("..", "Resources", "election_data.csv")

c1 = []
c2 = []
c3 = []
with open(path) as electiondatafile:
    csvreader = csv.reader(electiondatafile, delimiter=",")
    csv_header = next(csvreader) 
    # print(csvreader)
    for row in csvreader:
        c1.append(row[0])
        c2.append(row[1])
        c3.append(row[2])

    print(f"```")
    print(f"Election Results")
    print(f"-------------------------")
    totalvotes = len(c1)
    print(f"Total Votes: {totalvotes}")
    print(f"-------------------------")
    uniquenames = set(c3)
    for item in uniquenames:
        print(f"{item}: {'%.4f'%(float((c3.count(item))/(totalvotes))*100)}% ({(c3.count(item))}) ")
    def most_frequent(c3): 
        return max(set(c3), key = c3.count) 
    print(f"-------------------------")
    print(f"Winner: {(most_frequent(c3))}") 
    print(f"-------------------------")
    print(f"```")