# Recursion - call the function inside the function definition

""" # Get & Set Recursion limit(How many times to execute the recursion fun)
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())"""


def python():
    print("Python")
    python()


python()

