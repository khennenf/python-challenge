fish = "halibut"

# Loop through each letter in the string
# and push to an array
letters = []
for letter in fish:
    letters.append(letter)
print(letters)

capital_letters = []
for letter in fish:
    capital_letters.append(letter.upper())
print(capital_letters)

july_temperatures = [87, 85, 92, 79, 106]
hot_days = []
for temperature in july_temperatures:
    if temperature > 90:
        hot_days.append(temperature)
print(hot_days)

# initializing lists 
test_keys = ["Rash", "Kil", "Varsha"] 
test_values = [1, 4, 5] 
  
# Printing original keys-value lists 
print ("Original key list is : " + str(test_keys)) 
print ("Original value list is : " + str(test_values)) 
  
# using naive method 
# to convert lists to dictionary 
res = {} 
for key in test_keys: 
    for value in test_values: 
        res[key] = value 
        test_values.remove(value) 
        break  
  
# Printing resultant dictionary  
print ("Resultant dictionary is : " +  str(res)) 