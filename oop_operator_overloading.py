# a = 1
# b = 2
# print(a + b)
# print(int.__add__(a, b))
# #    int_class.dunder_methods

class vegetables:

    def __init__(self, carrot, beans):
        self.carrot = carrot
        self.beans = beans

    def __add__(self, other):
        carrot = self.carrot + other.carrot
        beans = self.beans + other.beans
        return vegetables(carrot, beans)


v1 = vegetables(5, 3)
v2 = vegetables(7, 8)
v3 = v1 + v2  # here, we have implemented operator overloading concept with help of __add__ class method.
print(f"v3.carrot = {v3.carrot} \nv3.beans = {v3.beans}")
