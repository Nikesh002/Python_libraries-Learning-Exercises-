from collections import Counter

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

d = Counter(some_list)
duplicates = list([item for item in d if d[item]>1])

duplicates1 = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)
print(duplicates1)
