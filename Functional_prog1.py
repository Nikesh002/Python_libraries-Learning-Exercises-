def add(i, j):
    return i + j


a = add  # Here, 'a' is a object of 'add' function
res = a(1, 3)
print(res)


# return a function
def call(i, j):
    return add(i, j)


# pass function as argument
def pas(i, j, fn):
    return fn(i, j)


print(pas(5, 6, call))
