# Collections

# Lists:

# Lists are ordered collections of items, allowing duplicate values.
# Created using square brackets [] or the list() constructor.
# Elements can be accessed using indices, starting from 0.
# Mutable: Elements can be modified, added, or removed after creation.
# Common operations include appending, extending, slicing, and iterating.


a =[1,2,"hai"]
b = [1,7,8]
print("type: ",type(a))
print("value of list 1: ",a) 
# add elements in a row
a.append(5)
print(a)
# add element in middle
a.insert(1,8)           #insert(index_value,new_element)
print(a)
# replace element
a[0]="my_List:"  #l_name[index_value] = element
print(a)
# delete element
a.pop(0)           # pop(index_value)
print(a)
a.pop()            # if you not give any value it will delete last element
print(a)
# add list2 into list1
a.extend(b)
print(a)


# Tuples:

# Tuples are ordered collections of items, similar to lists, but they are immutable.
# Created using parentheses () or the tuple() constructor.
# Elements can be accessed using indices, like lists.
# Immutable: Once created, elements cannot be changed, added, or removed.
# Commonly used for representing fixed data, function return values, and multiple assignments.


a= (1,2,4,5,6)
print("type: ",type(a))
print("value of tuple: ",a) 
b=list(a)                               # we no modify tuple so we conver into list
b.insert(2,3)
a=tuple(b)                              # replace tuple
print("value of tuple: ",a)


# Sets:

# Sets are unordered collections of unique items.
# Created using curly braces {} or the set() constructor.
# No duplicate items are allowed; they automatically enforce uniqueness.
# Common operations include adding, removing, checking membership, and set operations like union and intersection.
# Useful for eliminating duplicates and testing membership efficiently.



fruits = {'apple', 'banana', 'orange', 'apple'}  # Duplicate 'apple' is automatically removed
print(fruits)  # Output: {'banana', 'orange', 'apple'}
# Adding Elements:
fruits.add('grape')    # Adding a single element
fruits.update({'kiwi', 'pear'})  # Adding multiple elements
print(fruits)  # Output: {'banana', 'orange', 'apple', 'grape', 'kiwi', 'pear'}
# Removing Elements:
fruits.remove('banana')  # Removing an element; raises an error if not found
fruits.discard('kiwi')   # Removing an element; no error if not found
print(fruits)  # Output: {'orange', 'apple', 'grape', 'pear'}
# Checking Membership:
print('apple' in fruits)  # Output: True
print('banana' in fruits)  # Output: False
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Set Operations:
union_set = set1 | set2       # Union of two sets
intersection_set = set1 & set2  # Intersection of two sets
difference_set = set1 - set2   # Difference of two sets (elements in set1 but not in set2)
symmetric_diff = set1 ^ set2   # Symmetric difference (elements in either set, but not in both)

print(union_set)         # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(intersection_set)  # Output: {4, 5}
print(difference_set)    # Output: {1, 2, 3}
print(symmetric_diff)    # Output: {1, 2, 3, 6, 7, 8}

# Set Comprehensions:
squared_numbers = {a for x in range(1, 6)}
print(squared_numbers)  # Output: {1, 4, 9, 16, 25}


# Dictionaries:

# Dictionaries are unordered collections of key-value pairs.
# Created using curly braces {} or the dict() constructor with key-value pairs.
# Keys are unique and must be hashable (strings, numbers, tuples); values can be of any type.
# Elements are accessed using keys, not indices.
# Mutable: Values can be modified, added, or removed based on their keys.



person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}


print(person)  # Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}

print(person)  # Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}

# Accessing Values

print(person['first_name'])  # Output: John
print(person.get('age'))     # Output: 30
print(person.get('gender', 'N/A'))  # Providing a default value if the key doesn't exist

# Modifying and Adding Entries:

person['age'] = 31  # Updating the age
person['gender'] = 'Male'  # Adding a new key-value pair
print(person)  # Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 31, 'city': 'New York', 'gender': 'Male'}


#Removing Entries:

del person['city']  # Removing the 'city' entry
print(person)  # Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 31, 'gender': 'Male'}


# Looping Through a Dictionary:

for key in person:
    print(key, person[key])


# Dictionary Comprehensions:

squared_numbers = {x:x**2 for x in range(1, 6)}
print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Nested Dictionaries:

students = {
    'Alice': {'age': 20, 'major': 'Computer Science'},
    'Bob': {'age': 22, 'major': 'Engineering'}
}
print(students['Alice']['major'])  # Output: Computer Science


# Dictionary Methods:

keys = person.keys()        # Get dictionary keys
values = person.values()    # Get dictionary values
items = person.items()      # Get key-value pairs as tuples

print(keys)    # Output: dict_keys(['first_name', 'last_name', 'age', 'gender'])
print(values)  # Output: dict_values(['John', 'Doe', 31, 'Male'])
print(items)   # Output: dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 31), ('gender', 'Male')])