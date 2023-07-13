# # Find the Prime factors
# try:
#     num = int(input(" Please enter a number = "))
#     prime = []
#     for i in range(1, num + 1):
#         count = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 count += 1
#         if count == 1:
#             prime.append(i)
#     factors = []
#     for n in prime:
#         if num % n == 0:
#             factors.append(n)
#     print(factors)
# except IOError as err:
#     print(" Input error")


import math

factors = []


# A function to print all prime factors of
# a given number n
def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n, print i ad divide n
        while n % i == 0:
            factors.append(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors.append(int(n))
    return factors


# Driver Program to test above function

n = 639
print(primeFactors(n))
