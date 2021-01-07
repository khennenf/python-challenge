import os
import csv
##### Counts the rows
path = os.path.join("..", "Resources", "budget_data.csv")

c1 = []
c2 = []
with open(path) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader) 
    for row in csvreader:
        c1.append(row[0])
        c2.append(row[1])
    # print(row[0] + "is rated " + row[1])
for ind, amount1 in enumerate(c2):
    print(f"[{ind}] {amount1}")
# changeindex = list({ind})
# print (ind)
# for x in range(ind):
#     print(amount1, (0+x), (x))
# for x in range(ind):
#     print(amount1, (0+x), (x))
# print (f"printingValues----------------------------------")
# for x in range(len(c2)):
#     print(c2[x])
# print (f"printingListofDates----------------------------------")
# for y in range(len(c1)):
#     print(c1[y])
# print (f"printingFunction----------------------------------")
# def createList (r1, r2):
#     return list(range(r1+0,r2+1))
# r1, r2 = x, y
# print(createList(r1, r2))
# print (f"printing----------------------------------")
# print(createList(x, x + y))
# print (f"printing----------------------------------")
# print(createList(0, x))
# print (f"printing----------------------------------")
# print(createList(0, y))
# print (f"printing----------------------------------")
# print(createList(x, y))
# print (f"printing----------------------------------")
c2int = list(map(int, c2)) ###This works to make the list an int 
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
diff_list = []
for i in range(1,len(c2int)):
    x = c2int[i] - c2int[i-1]
    diff_list.append(x)
print(diff_list)
print(sum(diff_list))
print(max(diff_list))
print(min(diff_list))
res = {} 
for month in c1: 
    for values in diff_list: 
        res[month] = values 
        diff_list.remove(values) 
        break  
print ("Resultant dictionary is : " +  str(res)) 
print(max([i for i in res.values()]))
print(max(res.items(), key=lambda x: x[1]))
print(min(res.items(), key=lambda x: x[1]))





# for x in range(len(mylist)):
#         print(mylist[x-10]) -(x + (x+x-1))