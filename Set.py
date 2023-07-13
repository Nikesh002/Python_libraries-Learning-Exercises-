# Set : it's a collection of the unordered unique elements within the {}.
set1 = {1, 2, 3, 4, 5, 1}
print("Set1 = ", set1)
set2 = {7, 8, 5, 4, 3, 52, 10}
print("Set2 = ", set2)
set3 = {2, 4, 5}
print("Set3 = ", set3)
print()
# add(item)
set1.add(6)
print("set1.add(6) = ", set1, end="\n")

# remove(item)
set1.remove(1)
print("set1.remove(1) = ", set1, end="\n")

# Intersection of the sets using '&' operator
print("set1 & set2 = ", set1 & set2)

# Union of the sets using 'union()'/'|'
print("set1.union(set2) = ", set1.union(set2))
print("set1 | set2 = ", set1 | set2)

# check if SetA is a subset of setB using : SetB.issubset(SetA)
print("set3.issubset(set1) = ", set3.issubset(set1))

# check if SetB is issuperset of setA using : SetA.issuperset(SetB)
print("set1.issuperset(set3) = ", set1.issuperset(set3))