# Static methods of class
# Count number of instances

# First version
'''
def sequence_of_Spam():
    print('Число созданных экземпляров класса', Spam.isNumber)

class Spam():
    isNumber = 0
    def __init__(self):
        Spam.isNumber = Spam.isNumber + 1

a = Spam()
b = Spam()
c = Spam()

sequence_of_Spam()
Spam.isNumber
'''

# Second version
'''
class Spam_static():
    isNumber = 0
    def __init__(self) -> int:
        print('initiated')
        Spam_static.isNumber = Spam_static.isNumber + 1
    def counter() -> None:
        print(Spam_static.isNumber)

    counter = staticmethod(counter)

x = Spam_static()
y = Spam_static()
z = Spam_static()
Spam_static.counter()   # 3
z.counter()             # 3
Spam_static.counter()   # 3
'''

# Third version
# Методы класса для подсчета экземпляров каждого класса

class Spam():
    numInstances = 0
    def count(cls):
        cls.numInstances += 1
    def __init__(self):
        self.count()
    count = classmethod(count)

class Sub(Spam):
    numInstances = 0
    def __init__(self):
        Spam.__init__(self)

class Other(Spam):
    numInstances = 0

x = Spam()
x1, y1 = Sub(), Sub()
x2, y2, z2 = Other(), Other(), Other()

x.numInstances, y1.numInstances, x2.numInstances