# Create a dictionary

# empty dictionary
my_dict = {}
print("Empty dictionaryy:")
print(my_dict)

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
print("\nDictionary with the use of integer keys:")
print(my_dict)

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
print("\nDictionary with the use of mixed keys:")
print(my_dict)

# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print("\nDictionary with the use of dict():")
print(my_dict)

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print("\nDictionary with each item as a pair:")
print(my_dict)


# Access Elements from a Dictionary
print("\nAccess Elements from a Dictionary")
my_dict = {'name':'Jack', 'age': 26}
print(my_dict['name'])
print(my_dict.get('age'))


# Add elements in a dictionary
my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27
print(my_dict)

# add item
my_dict['address'] = 'Downtown'
print(my_dict)

# Delete or remove elements from a dictionary

# Create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

# remove a particular item
print(squares.pop(4))
print(squares)

# delete a particular item
del squares[5]
print(squares)

# remove all items
squares.clear()
print(squares)