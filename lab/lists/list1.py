# lists

# Create lists
# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed data types
my_list = [1, "Hello", 3.4]

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]



# Access list elements by index
# List indexing
my_list = ['p', 'r', 'o', 'b', 'e']

# Output: p
print(my_list[0])

# Output: ?
print(my_list[2])

# Output: ?
print(my_list[4])

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
# Output: a
print(n_list[0][1])

# Output: ?
print(n_list[1][3])

# Error! Only integer can be used for indexing
print(my_list[4.0])

# Negative indexing in lists
my_list = ['p','r','o','b','e']

# Output: e
print(my_list[-1])

# Output: ?
print(my_list[-5])

# Slice
# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']

# elements 3rd to 5th,
# from index 2, 3 elements
print(my_list[2:5])

# from index 0 to the element before index -5
print(my_list[:-5])

# index 5 (elements 6th) to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])






# Correcting mistake values in a list
odd = [2, 4, 6, 8]
# add or change
# change the 1st item
odd[0] = 1

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd)

# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)

# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])

print(["re"] * 3)

# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)

print(odd)

odd[2:2] = [5, 7]

print(odd)

#delete remove
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete entire list
del my_list

# Error: List not defined
print(my_list)

# Remove
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Pop
# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

# Clear
my_list.clear()

# Output: []
print(my_list)