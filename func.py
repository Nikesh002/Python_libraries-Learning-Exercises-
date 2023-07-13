def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def square(z):
    return z * z


# Passing arguments to a function
ans = div(12, 20)
print(ans)
# Passing function as argument
print(square(add(3, 4)))
