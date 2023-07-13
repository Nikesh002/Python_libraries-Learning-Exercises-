"""# Iterator & Generator

# list = [n for n in range(6)]
# iteration = iter(list)
# print(iteration.__next__())
# print(iteration.__next__())
# print(next(iteration))
# print()


# Generator
def fn():
    yield 1
    yield 2
    yield 3


values = fn()
# print(values)
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())

for i in values:
    print(i)
"""


# w.a.p. to generate the square of 1 to 5 numbers

def square():
    n = 1
    while n < 6:
        yield n ** 2
        n += 1


for i in square():
    print(i)
