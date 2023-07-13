# map(function, iterable)

numbers = [n for n in range(1, 6)]

print("numbers = ", numbers)
# Use map() to get the square of the given list
print("map() = ", list(map(lambda n: n ** 2, numbers)))
