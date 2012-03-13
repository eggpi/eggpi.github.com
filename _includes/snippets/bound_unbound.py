class Num(object):
    def __init__(self, amount):
        self.amount = amount

    def double(self):
        return self.amount * 2

def triplicate(self):
    return self.amount * 3

num2 = Num(2)
print num2.double()

Num.double = triplicate
print num2.double()

num2.double = triplicate
print num2.double()
