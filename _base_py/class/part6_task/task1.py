class Adder:
    def __add__(self, other):
        if type(other) is list:
            return self.add(other)
        elif type(other) is dict:
            pass
        else:
            print('Not Implemented')
        

class ListAdder(Adder):
    # def __init__(self, value) -> None:
    #     self.value = value
    # def __add__(self, other):
    #   self.data = super().__add__(other)
        # Adder.__add__(self, other)
    def add(self, other):
        return self.value + other


class DictAdder(Adder):
    # def __add__(self, **kwargs):
    #     super().__add__()
    def add(self, other):
        c = {}
        for ela in self.value: c[ela] = self.value[ela]
        for elb in other:  c[elb] = other[elb]
        print(c)
        return c

d1 = DictAdder()
d1.value = {'a': 1, 'b': 2, 'c': 3}
# d1.value + {'key': 365, 'push': 487}


# a = {'a': 1, 'b': 2, 'c': 3}
b = {'key': 365, 'push': 487}
d1.add(b)
# c = {}



    
# print(c)

l1 = ListAdder()
l1.value = [1,2,3]
y = l1 + [4,5,6]
print(y)