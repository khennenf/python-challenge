# july_temperatures = [87, 85, 92, 79, 106]
# hot_days = []
# for temperature in july_temperatures:
#     if temperature > 90:
#         hot_days.append(temperature)
# print(hot_days)

import os
import csv
##### Counts the rows
path = os.path.join("..", "Resources", "election_data_short.csv")

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
        print (f"printingValues----------------------------------")
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

#     # not_marsh_votes = []
#     # for county in c2:
#     #     if county != "Marsh":
#     #         not_marsh_votes.append(county)
#     # print(not_marsh_votes)
#     # candidatevotes = []
#     # for candidate in c3:
#     #     if candidate != "Khan":
#     #         candidatevotes.append(candidate)
#     # print (f"printinglast----------------------------------")            
#     # print(f"{candidatevotes} {not_marsh_votes}")

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



