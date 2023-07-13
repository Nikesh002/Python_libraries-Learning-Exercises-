# Tuple
t1 = (12, 22, 13, 4, 5)
print(type(t1))
print("t1 = ", t1)

t2 = ('mom', 'dad')
print("t2 = ", t2)
print(t1 + t2)

print("len(t1) = ", len(t1))

# Tuples are Immutable
# t1[0] = 9
# print(t1)

# sorted()
tup_sort = sorted(t1)
print("sorted(t1) = ",tup_sort)

# index(item)
print("t1.index(13) = ",t1.index(13))
