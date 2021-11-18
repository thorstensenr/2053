# Create a dictionary of people's favorite foods called fav_food_map
favorite_foods = {}
favorite_foods['kathleen'] = 'pizza'
favorite_foods['steve'] = 'ribs'
favorite_foods['john'] = 'chili'
favorite_foods['michelle'] = 'pasta'
favorite_foods['patrick'] = 'ice cream'

# iterate through map
# first print just the key
for key in favorite_foods:
    print(key)

# use the .values() method to print values only
for value in favorite_foods.values():
    print(value)

# Now use the key to get the value and print key and value
for key in favorite_foods:
    print(key, "favorite food is", favorite_foods[key])

# Use .items() that returns a tuple and assign tuple to key, value
for key, value in favorite_foods.items():
    print(key, "favorite food is", value)

# Check if key is in dictionary
if 'Mary' in favorite_foods:
    print("Mary's fav food is ", favorite_foods['Mary'])
else:
    print("Mary not in dictionary")

# Dictionaries do not allow duplicate keys
# Using the key kathleen again will overwrite the original value
favorite_foods['kathleen'] = 'cake'
print(favorite_foods)

# delete item from dictionary using key
del favorite_foods['kathleen']
print(favorite_foods)

# Dictionary use case
# Given a list of foods, count the number of times each food shows up in list of foods
# Store the results in a dictionary with the food name as the key and number as value
food_list = ['pizza', 'taco', 'ice cream', 'bagels', 'butter', 'butter', 'pizza', 'pizza']
food_num = {}
for food in food_list:
    if food in food_num:
        food_num[food] += 1
    else:
        food_num[food] = 1
print(food_num)

# Create a dictionary using comprehensions
key_list = ["cat", "dog", "cow"]
new_dict = {key: 1 for key in key_list}
print(new_dict)

# Can use a tuple to assign keys and values
keys = ['one', 'two','three']
values = [1,2,3]
zipped = zip(keys, values)
pairs = {key: value for key, value in zipped}
print("pairs")
print(pairs)

# Create a new dictionary with the values as the keys and keys are values
# {1: "one", 2: "two"}
flipped_pairs = {key: value for value, key in pairs.items()}
print(flipped_pairs)

# deans list - write a function that takes a dictionary of names mapped to GPA and return a
# set of names that made the deans list (GPA >= 3.5)
# Use a comprehension
grades = {"Joe": 3.5, "Jane": 4.0, "Jenny":3.8, "Rahul": 3.9, "Raj": 3.0}
deans_list = {key for key, value in grades.items() if value >= 3.5}
print(deans_list)

# write a function that takes a dictionary with city name as key and zip code as value.
# return a new dictionary with zip code as key and a list of cities with the zip code.
zips = {}
city_zips = {"Dunmore": 18509, "Scranton": 18509, "Rye": 10580, "San Francisco": 94016, "Devon": 19087, "Wayne":19087}
for key, value in city_zips.items():
    if value in zips:
        zips[value].append(key)
    else:
        zips[value] = [key]
print(zips)