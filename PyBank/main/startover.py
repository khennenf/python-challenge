import os
import csv

cereal_csv = os.path.join("..", "Resources", "budget_data.csv")


# Open and read csv
c1 = []
c2 = []
with open(cereal_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    mylist = list(csv_reader)

    for x in range(len(mylist)):
        print(mylist[x-10])
    
#     found = False
#     amount = input("What amount are you looking for? ")
    
    
#     # Read through each row of data after the header
#     # for row in csv_reader:
#     #     # Convert row to float and compare to grams of fiber
#     #     if int(row[1]) >= 989499:
#     #         print(row)
#     # for row in csv_reader:
#     #     if row[1] == amount:
#     #         print(f"The amount is {row}")
#     #This gives you the total of the whole column:
    
#     total = 0
#     for row in csv_reader:
#         total += int(row[1])
#     print(f"Total: ${total}")
# #---------------------------------------------------------------
# with open(cereal_csv) as budgetfile:
#     csvreader = csv.reader(budgetfile, delimiter=",")
#     csv_header = next(csvreader)
#     data = list(csvreader)
#     row_count = len(data)
#     print(f"Total Months: {row_count}")


#---------------------------------------------------------------
# c1 = []
# c2 = []
# with open(cereal_csv) as budgetfile:
#     csvreader = csv.reader(budgetfile, delimiter=",")
#     csv_header = next(csvreader)
#     for i in csvreader:
#         c1.append(i+1,[0])
#         c2.append(i+1, [1])
#     print(i[0] + "is rated " + i[1])
# # for ind, amount1 in enumerate(c2):
#     print(f"[{ind}] {amount1}")
# for x in range(len(c2)):
# #     print(c2[x])


# c1 = []
# c2 = []
# with open(cereal_csv) as budgetfile:
#     csvreader = csv.reader(budgetfile, delimiter=",")
#     csv_header = next(csvreader)
#     for i in csvreader:
#         print(i.as_void())






    





    


