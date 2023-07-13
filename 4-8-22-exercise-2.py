# Exercise: Check for the duplicates in list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

some_list.sort()

for i in range(len(some_list)-1):
    if str(some_list[i]) == str(some_list[i+1]):
        print(" '{}' is repeated. ".format(some_list[i]))

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
