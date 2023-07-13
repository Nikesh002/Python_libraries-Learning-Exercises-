''' Using normal for loop'''
# fib_list = [0, 1, 1]
#
#
# def fib(num):
#     n1 = 1
#     n2 = 1
#     for i in range(num-2):
#         fib_list.append(n1 + n2)
#         temp = n1
#         n1 = n2
#         n2 = temp + n2
#     return fib_list
#
#
# print(fib(20))

'''Using generator + Output in List'''
n = 20
fib_list = []


def fibonacci_generator(num):
    n1, n2 = 0, 1
    count = 0
    while count <= num:
        yield n1
        fib_list.append(n1)
        n1, n2 = n2, n1 + n2
        count += 1


for i in fibonacci_generator(n):
    print(i, end="\t")
print("\n", fib_list)


