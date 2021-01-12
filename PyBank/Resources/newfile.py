import os
import csv
import sys
#File Path
path = os.path.join("..", "Resources", "budget_data.csv")
#Declare columns to lists
c1 = []
c2 = []
#Open File
with open(path) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader) 
    for row in csvreader:
        #(add rows to columns)
        c1.append(row[0])
        c2.append(row[1])
c2int = list(map(int, c2)) ###Changes list to int
# print (f"printing----------------------------------")
# print(createList(x, y))
# print (f"printing----------------------------------")
# c2int = list(map(int, c2)) ###This works to make the list an int 
print(c2int) ###This works to make the list an int 
print (f"printingValuesAsIntenger----------------------------------")
# for x in range(len(c2int)):
#     print(c2int[x])
# print (f"printingValuesAsResult----------------------------------")
# result = []
# for x in range(len(c2int)):
#     result.append(c2int[x])
# print(result)
# for x in range(len(c2int)):
#     print(c2int[x] + r1 + r2)
print (f"printingValuesDifferent List----------------------------------")
# for x in amount1:
#     # for y in c2int:
# #             print(x,)
print(f"---------------Yeah! This works!")
import os
import csv
import sys
#File Path
path = os.path.join("..", "Resources", "budget_data.csv")
#Declare columns to lists
c1 = []
c2 = []
#Open File
with open(path) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader) 
    for row in csvreader:
        #(add rows to columns)
        c1.append(row[0])
        c2.append(row[1])
c2int = list(map(int, c2)) ###Changes list to int
total_months = len(c1)
total_amount = sum(c2int)
months_average = total_months - 1
c1.pop(0)
print(f"This is months list {c1}")
diff_list = []
#Get difference between months
for i in range(1,len(c2int)):
    x = c2int[i] - c2int[i-1]
    diff_list.append(x)
print(f"What does this print  {min(diff_list)}")
mydictionry = dict(zip(c1, diff_list))
print(mydictionry)
print(min(diff_list))
sum_month_change = sum(diff_list)
print(f"this is the monthly change: {sum_month_change}")
print(diff_list)
# diff_list1 = {diff_list, c1}
# print(diff_list1)
# print(d)
#delete first row
c1.pop(0)
#create dict of items
valuesdict = {} 
for month in c1: 
    for values in diff_list: 
        valuesdict[month] = values
        # diff_list.remove(values) 
key, value = max(mydictionry.items(), key=lambda x:x[1])
print(f"This is the key and value: {key, value}")
# print(f"THis is the values dictionary:= {valuesdict}")
# print(f"This is new forumla: {min(valuesdict, key = lambda n : valuesdict.get(n))}")
# print(f"{max(valuesdict.items(), key = lambda k : k[1])}")

# maxvalue = (max(.items(), key=lambda x: x[0]))
# maxvalue = (max(valuesdict.items(), key=lambda x: x[0]))
# print(maxvalue)
# print(maxvalue)
# [mmax, vmax  = maxvalue
# mmin, vmin = minvalue]
average_change = sum_month_change/months_average
average_change_decimal = round(average_change, 2) 
print(f"```text")
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_change_decimal}")
# print(f"Greatest Increase in Profits: {mmax} (${vmax})")
# print(f"Greatest Decrease in Profits: {mmin} (${vmin})")
print(f"```")

sys.stdout = open('/Users/keri.ROGUE/Desktop/python-challenge/PyBank/analysis/output.txt', 'wt') 
print(f"```text")
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_change_decimal}")
# print(f"Greatest Increase in Profits: {mmax} (${vmax})")
# print(f"Greatest Decrease in Profits: {mmin} (${vmin})")
print(f"```")