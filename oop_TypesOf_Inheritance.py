# Types of Inheritance

# Single-Level Inheritance
# Multi-Level Inheritance
# Multiple Inheritance

"""# 1 - Single-Level : 1 Parent Class <--> 1 Child Class

class A:
    def state_1(self):
        print("State_1 present")

    def state_2(self):
        print("State_2 present")

    def state_3(self):
        print("State_3 present")


class B(A):
    def state_4(self):
        print("State_4 present")

    def state_5(self):
        print("State_5 present")


a = A()
a.state_1()
a.state_2()

b = B()
b.state_4()
b.state_3()
"""


"""# 2 - Multi-Level : it's like a series of Single-Level Inheritance e.g. Class A --> Class B --> Class C

class A:
    def state_1(self):
        print("State_1 present")

    def state_2(self):
        print("State_2 present")

    def state_3(self):
        print("State_3 present")


class B(A):
    def state_4(self):
        print("State_4 present")

    def state_5(self):
        print("State_5 present")


class C(B):

    def state_6(self):
        print("State_6 present")


c = C()
c.state_3()
c.state_4()
c.state_6()
"""

# 3 - Multiple Inheritance : More the One parent classes <--> One Child class

class A:
    def state_1(self):
        print("State_1 present")

    def state_2(self):
        print("State_2 present")

    def state_3(self):
        print("State_3 present")


class B:
    def state_4(self):
        print("State_4 present")

    def state_5(self):
        print("State_5 present")


class C(A,B):

    def state_6(self):
        print("State_6 present")

a = A()
a.state_2()

b = B()
b.state_4()

c = C()
c.state_1()
c.state_4()
c.state_6()
