"""# Dictionary creation
my_dict = {'key1': 'value1', 1: 'str', 2: 2.3, 3: (1, 2.5, 'xyz'), 4: [2, 5.2, 'abc']}
# Accessing specific element from the my_dict
print(my_dict)
print(my_dict[3])
print(my_dict[3][1])"""

# Dictionary functions
my_dict1 = {'a': 'apple', 'b': 'ball', 'c': 'cat', 'd': 'dog'}
print(my_dict1)
# adding new element to the dictionary
my_dict1['e'] = 'elephant'  # dict['key'] = 'value'
# deleting a specific entry from the dictionary
del(my_dict1['c'])
print(my_dict1)
# Check if the specific key/value is present in the dictionary
print('a' in my_dict1)  # matching for key
print('g' in my_dict1)
print('ball' in my_dict1.values())  # matching for value
# Print Keys, Values & Items of the Dictionary
print(my_dict1.keys())
print(my_dict1.values())
print(my_dict1.items())
# get('key') : it returns value if the key is present in the dictionary else return None.
print(my_dict1.get('b'))

