# filter (function, iterable)
# Here, function will give True/False result based on the passed iterator from the iterable
# & only True results will be stored.

# only print the even numbers from the list
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list((filter(lambda n: not n % 2, range(11)))))
