#* The winner of the election based on popular vote.
#Winner: Khan
import os
from collections import OrderedDict
import csv
path = os.path.join("..", "Resources", "election_data_short.csv")

# ######Get unique values
# import os
# import csv
# ##### Counts the rows
# path = os.path.join("..", "Resources", "election_data_short.csv")

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
    # for county in c2:
    #     print(county)
    # print(c1)
    # print(c2)
    # print(c3)
c1int = list(map(int, c1)) ###Changes list to int
a = [c1int] 
b = [c2]  
c = [c3]  

result = zip(a, b, c)
print(result)

new_dict_3 = {result}
print(new_dict_3)
# for a in result:
#     print(f"This is {a} ; This is {b}")

# new_dict = dict(zip(c1int, c2))
# print(new_dict)

# new_dict_2 = dict(zip(new_dict, c3))
# print(new_dict_2)

# for i in new_dict_2:
#     print(i, j)

# new_dict = {}
# i:[j, k] for i, j, k in zip(a, b, c)}

# valuesdict = {} 
# for month in c1: 
#     for values in diff_list: 
#         valuesdict[month] = values 
#         diff_list.remove(values) 



    # for row in csvreader:
    #     print(row)
# numbers = [ c1]
# def get_unique_numbers(numbers):
#     list_of_unique_numbers = []
#     unique_numbers = set(numbers)
#     for number in unique_numbers:
#         list_of_unique_numbers.append(number)
#     return list_of_unique_numbers
# # print(get_unique_numbers(numbers))
# numlist = (get_unique_numbers(numbers))
# print(numlist)
# for name in enumerate(numlist):
#     print(f"{name}")
# for x in numlist:
#     print(f"This is a {x}")

# numlist = (get_unique_numbers(numbers))
# print(numlist)
# for name in enumerate(numlist):
#     print(f"{name}")
# for x in numlist:
#     print(f"This is a {x}")

# votesdict = {}
# for votes in c1: 
#     for values in diff_list: 
#         valuesdict[month] = values 
#         diff_list.remove(values) 