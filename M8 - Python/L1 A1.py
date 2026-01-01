lst = ['Apple', 'Banana','Mango','Guava','Kiwi']
print("Length of list:", len(lst))
print("First Element:", lst(0))
print("Last Element", lst[-1])

lst.append['Orange']
print(lst)

lst.remove['Guava']
print('Updated list:', lst)

#Sorts in alphabetical order
lst.sort()
print('Sorted list:', lst)

#Removes item with index number
lst.pop(2)
print(lst)

lst.reverse()
print(lst)


#Repeats the items in a list by the number of times multiplied
lst = lst*2
print("Multiplication of list", lst)

#Only print the items with the corresponding index values, 2,3,4 since n-1
lst = lst[2:5]
print('Sliced list:', lst)

lst.clear()
print(lst)