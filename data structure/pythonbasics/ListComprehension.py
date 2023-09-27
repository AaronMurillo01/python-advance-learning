# List comprehension: allows us to create a new list based on existing values of another list

# numbers = [1, -5, 0, 10, 100, 67, 55, 20, 34]

names = [ 'Adam', 'Kevin', 'Stephen', 'Daniel', 'Joe', 'Maria', 'Adele' ]

filtered_name = []

#we want to get the name with 4 letters
filtered_name = [name for name in names if len(name) == 4]

# filtered_name = [name for name in names if name.startswith('A')]
        
print(filtered_name)        

# for name in names: 
#     if name.startswith('A'):
#         filtered_name.append(name)

# new_list = [num for num in numbers if num % 2 == 0]

# for num in numbers: 
#     if num % 2 == 0:
#         new_list.append(num)
        
# print(new_list)        