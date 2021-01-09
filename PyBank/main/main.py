import os
import csv
import sys
path = os.path.join("..", "Resources", "budget_data.csv")
c1 = []
c2 = []
with open(path) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader) 
    for row in csvreader:
        c1.append(row[0])
        c2.append(row[1])
c2int = list(map(int, c2)) ###Changes list to int
total_months = len(c1)
total_amount = sum(c2int)
months_average = total_months - 1
diff_list = []
for i in range(1,len(c2int)):
    x = c2int[i] - c2int[i-1]
    diff_list.append(x)
sum_month_change = sum(diff_list)
c1.pop(0)
valuesdict = {} 
for month in c1: 
    for values in diff_list: 
        valuesdict[month] = values 
        diff_list.remove(values) 
minvalue = (min(valuesdict.items(), key=lambda x: x[1]))
maxvalue = (max(valuesdict.items(), key=lambda x: x[1]))
mmax, vmax  = maxvalue
mmin, vmin = minvalue
average_change = sum_month_change/months_average
average_change_decimal = round(average_change, 2)
print(f"```text")
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total$: ${total_amount}")
print(f"Average Change: ${average_change_decimal}")
print(f"Greatest Increase in Profits: {mmax} (${vmax})")
print(f"Greatest Decrease in Profits: {mmin} (${vmin})")
print(f"```")

sys.stdout = open('output.txt', 'wt')
print(f"```text")
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total$: ${total_amount}")
print(f"Average Change: ${average_change_decimal}")
print(f"Greatest Increase in Profits: {mmax} (${vmax})")
print(f"Greatest Decrease in Profits: {mmin} (${vmin})")
print(f"```")








