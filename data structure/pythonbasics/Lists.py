#usually this is called an array - but in python it is called a list
#if you want to use an array - than you use NumPy array
my_list =["My name is Aaron!", 10, 4.5]

# print(my_list)
# print (len(my_list))
# print(type(my_list))
my_list[0] = "My name is not Edwin!"
my_list[1] = 15

for item in my_list:
    print(item)
    
# del operator will remove a given item
del my_list[0]

print(len(my_list))
print(my_list)

#appending a new item at the end of the list is 0(1)
my_list.append("This is a new item!")

# because lists are indexed, there may be multiple items with the same value
my_list.append("This is a last item!")

print(my_list[0:2])

print(25*"-")

list1 = [1, "This is the list1", 3.5]
list2 = [True, "This is the list2", False]

# result = list1 + list2
list1.extend(list2)
print(list1)
# print(result)
# print(my_list)

# the list's built-in functions
list1.append('A new item')
print(list1)
# list1.remove(3.5)
# list1.remove('This is the list2')
# pop () function return and remove the last item in the list...
# this is 0(1) because we manipulate the last item
# result = list1.pop()
list1.reverse()
print(list1)

# list_name = ["Anna", "Kevin", "Stephen", "Daniel", "Adam", "Joe", "Maria", "Adele" ]
list_name = [45, 3, -5, 12, 15, 8, 7, 7, -5, 0, 1]
list_name.sort()
print(list_name)
# result = list1.copy()
# print(result)