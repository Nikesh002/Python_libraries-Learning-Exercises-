class User():
    def sign_in(self):
        print(" Logged in. ")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def check_power(self):
        print(f' {self.power} remaining.')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f' {self.arrows} remaining.')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridBorg('borgie', 50, 100)
hb1.sign_in()
hb1.check_power()
hb1.check_arrows()
