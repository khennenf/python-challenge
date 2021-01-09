# july_temperatures = [87, 85, 92, 79, 106]
# hot_days = []
# for temperature in july_temperatures:
#     if temperature > 90:
#         hot_days.append(temperature)
# print(hot_days)

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
        #   
#   for county in c2:
#         print(county)
#     res = {} 
#     for id in c1: 
#         for county in c2: 
#             for candidate in c3:
#                 res[id] = county
#                 # c2.remove(county) 
#                 county = candidate
#                 c3.remove(candidate)
#         break  
#   # Printing resultant dictionary  
# print ("Resultant dictionary is : " +  str(res))   
# for v in res.values():
#     print(v)
# for county in c2:
#     print(county)
    # not_marsh_votes = []
    # for county in c2:
    #     if county != "Marsh":
    #         not_marsh_votes.append(county)
    # print(not_marsh_votes)
    # unique = OrderedDict((x,1) for x in c3).keys()
    # for candidatename in unique:
    #         print(candidatename)
    # print(unique)
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
    # candidatevotes = []
    # for candidate in c3:
    #     if candidate == "Khan":
    #         candidatevotes.append(candidate)
    #     # print(candidatevotes)
    # print (f"printinglast----------------------------------")    
    # # a = unique
    # # b = c3
    # # for x, y in [(x,y) for x in b for x in a]:
    # #     print(f"printing_____________ {x}")        
    # # # print(f"{candidatevotes} {not_marsh_votes}")
    # khanvotes = len(candidatevotes)
    # print(f"Votes for Khan: {khanvotes}")
    # totalvotes = len(c1)
    # print (f"Total votes are: {totalvotes}")
    # khanpercent = khanvotes/totalvotes
    # print(khanpercent)
    # khannumpercent = ((khanpercent)*100)
    # print(round(khannumpercent, 4))
    # khannumpercentrnd = round(khannumpercent, 4)
    # print(f"Percentage for Khan is {khannumpercentrnd}")
    # print ("{0:.4f}". format(khannumpercent)) #will add 0 after decimal point for int values.

#     # # initializing lists 
# # test_keys = ["Rash", "Kil", "Varsha"] 
# # test_values = [1, 4, 5] 
  
# # # Printing original keys-value lists 
# # print ("Original key list is : " + str(test_keys)) 
# # print ("Original value list is : " + str(test_values)) 
  
# # using naive method 
# # to convert lists to dictionary 



























# import csv

# path = os.path.join("..", "Resources", "election_data_short.csv")

# infile = open('election_data_short.csv', 'r')
# import csv
# table = []
# for row in csv.reader(infile):
#     table.append(row)
# table = [row for row in csv.reader(infile)]
# print(table)



# infile = open('election_data_short.csv' , 'r')
# data = {}
# data['data'] = {}
# for line in infile:
#     columns = line.split()
# voter = str(columns[0])
# county = str(columns[-1])
# candidate = str(columns[-1])
# print(candidate)
# print(voter)
# print(county)



