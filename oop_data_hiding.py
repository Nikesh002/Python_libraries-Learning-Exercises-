# Data Hiding : We just need add '__' as a prefix for the class attributes & methods to hide it/make it private.
# The only owner of the class can view the private/hidden attributes & methods [_ClassName__attribute/method_Name]
# OR with the help of dir() to get to know the
# correct name of the __attribute/__methods e.g. here __value_1 can be access via s._Simple__value_1
class Simple:
    def __init__(self):
        self.__value_1 = 1
        self.value_2 = 2

    def __A1_(self):  #
        print("apple")

    def _B2_(self):  # here, _B2_ can be access by public view
        print("ball")


s = Simple()
# print(s.__value_1)
print(s._Simple__value_1)
s._B2_()
s._Simple__A1_()
# s.__A1_()
print(dir(s))  # dir(s) : with this we can get all the publicly accessed methods/attributes of object of 's'
