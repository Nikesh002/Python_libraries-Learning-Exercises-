class Name:
    name = ""

    def __init__(self, name):
        self.name = name
        print("Hi ", name)


class FootballFans(Name):
    points = 0

    def __init__(self, name, points):
        super().__init__(name)
        self.points = points

    def pts(self):
        print(f"{self.name} scores = {self.points}")


n = Name("Sam")
f = FootballFans("Jim", 5)
f.pts()
