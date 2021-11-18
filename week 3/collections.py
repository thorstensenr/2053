list1 = [1, 2, 3, 4, 5]

# Create a list of 10 elements all with the number 5
repetition = [5] * 10
print(repetition)
# copy all elements to list1_copy
list1_copy = list1[:]

# If you change an element in the copied list it only changes the value there
# The original list is unchanged
list1_copy[2] = 300
print(list1)
print(list1_copy)

# Copy elements 1 - 3 to a new list
mid_list = list1[1:4]
print(mid_list)

# Create a new list with the first two elements removed
remove_first_two = list1[2:]

# Copies all elements up to the last two elements
remove_last_two = list1[:-2]
print(remove_first_two)
print(remove_last_two)

# How would you add last two elements to a new list?
last_two_only = list1[-2:]
print(last_two_only)

# Slice elements 2 and 3 to a new list
two_three = list1[2:4]
print(two_three)

# Use the extend method to add a list of elements to list
list2 = [10, 20, 30]
list3 = [100, 200, 300]
list1.extend(list2)
print(list1)
list1.append(list3)
print(list1)
# Notice the difference between extend and add
# extend adds each element to the list
# append adds the list as one new element to the list

# index method returns the index place of an element in the list
# count returns the number of times the element shows up in the list
# try this out with an element in the list and one not in the list. what does it return?
print(list1.index(4))
# print(list1.index(1000))
print(list1.count(4))
# print(list1.count(1000))

# index and count throw exceptions, first check if element is in list
if 1000 in list1:
    print(list1.index(1000))
    print(list1.count(1000))
else:
    print("1000 not in list")

# Use a for loop to create a list of size 10 of even numbers starting at 2
list_even = []
for i in range (2, 22, 2):
    list_even.append(i)
print(list_even)

# Now do the same using comprehension
list_even1 = [i for i in range(2, 22, 2)]
print(list_even1)

# Create a new list with elements 0 - 50
new_list = [i for i in range(0,51)]
print(new_list)

# Now add odd numbers to a new list
odd_list = [i for i in new_list if i % 2 != 0]
print(odd_list)

# Create 2D list and access all elements
# Must first fill list with elements. Use comprehension for this.
num_rows = 10
num_cols = 5
# Use repetition to create a list for each row in 2D list
two_d = [[0] * num_cols for i in range(0, num_rows)]
# Loop through to change elements and print
for row in range(len(two_d)):
    for col in range(len(two_d[row])):
        two_d[row][col] = row * row
        print(two_d[row][col],' ',end='')
    print()


# A tuple is used when you want an immutable list
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(weekdays)

# Assign values to multiple variables using a tuple
coordinates = (5, 25)
x, y = coordinates
print(x, y)

# Sets
# Sets do not allow duplicates
dup_list = [i for i in range(0,5)]
dup_list.extend(dup_list)
print((dup_list))

set1 = set(dup_list)
# duplicate elements are removed
print(set1)

# There is no order of the elements. Can't use index place to access. Must use loop
for num in set1:
    print(num)

# Create set
new_set1 = {10, 20, 50}

# Create an empty set
empty_set2 = set()
print(new_set1)
print(empty_set2)

# Add elements to each set
new_set1.add(25)
empty_set2.add(30)
print(new_set1)
print(empty_set2)