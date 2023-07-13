# Lists are Mutable(changeable)
list1 = ['mike', 10.1, 1980]
list2 = ['pop', 1]

# Adding 2 lists into one
list3 = list1 + list2
print(list3)

# Multiplying by 2
print(list2 * 2)

# Replacing the list item
list3[3] = 'Wong'
print(list3)

# Check if the given item present in the List
print('pop' in list3)

# append() : with this, we can just add single value at a time to the list
list3.append('Tom')
print('append(\'Tom\') = ', list3)

# extend(iterable) : with this, we can add multiple values to the list
# iterable: Any iterable (list, set, tuple, etc.)
list3.extend([False, 3.14, 5])
print('extend([False, 3.14, 5]) = ', list3)

# remove(list_item) : to remove the specific item from the list
list3.remove(5)

# del(start_index:end_index) : with this, we can delete sub list from the list
del list1[0:2]
print('del list1[0:2] = ', list1)

# clear() : it deletes every element from the list
list2.clear()
print(list2)

# pop(index) : with this, we can remove the specific index value from the list.
# if we didn't give the value then, by default it will remove last element from the list
print(list3.pop(2))

# insert() : we place specific value at the specific index of the list

list3.insert(2, 'Ram')
print(list3)

# sort()
list4 = [10.2, 1985, 9, 15]
list4.sort()
print("Sorted list = ", list4)

# reverse()
list4.reverse()
print("Reverse sorted list = ", list4)

# index(value) : it returns the index of the given value if that is part of the list
print("Index(15) = ", list4.index(15))

# len(iterator) : it returns length of the list
print("len(list4)", len(list4))

# List slicing : it used to form new sub-list from the existing list
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list5)
print("List slicing = ", list5[4:5])
print("List slicing = ", list5[6:])
print("List slicing = ", list5[::2])

# List comprehension
# Syntax : [expression for item in list {if {condition}}]
list6 = [n for n in range(1, 11) if n % 2]
print(list6)

# generate the list using list comprehension
print([i ** 2 for i in range(1, 11) if not i % 2])
