my_dict = {}

my_dict = {1:'apple', 2:"ball"}
my_dict = {'name':'John', 1:[2,4,3]}

my_dict = {'name': 'John', 'age': 27}

print(my_dict['name'])
print(my_dict.get('name'))  #Same as prev line

#Updating an existing key
my_dict['age'] = 28
print(my_dict)

#Adding an item
my_dict['address'] = 'Downtown'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address:", my_dict.get('address'))

my_dict.clear
print(my_dict)