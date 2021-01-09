#* The winner of the election based on popular vote.
#Winner: Khan
import os
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
    for county in c2:
        print(county)
    for i in range(len(c2)):
        print(c2[i])
    # mylistint = list(map(int, c2))
    # for x in range(mylistint):
    #     print(f"This is a {x}")

#     # for row in csvreader:
#     #     print(row)
# numbers = [ "k", "k", "k", 22, 90, 12, 2]
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