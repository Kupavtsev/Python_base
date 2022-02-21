class FirstClass():
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)
        #print(self.another)

class SecondClass(FirstClass):
    def display(self):
        print('This is SecondClass = "%s"'  % self.data)

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: "%s"]' % self.data
    def mul(self, other):
        self.data *= other

a = ThirdClass("abc")
a.display()     # "abc"
print(a)        # [ThirdClass: "abc"]
b = a + 'xyz'
print(b)        # [ThirdClass: "abcxyz"]
a.mul(3)        
print(a)        # [ThirdClass: "abcabcabc"]
    

x = FirstClass()
y = FirstClass()

x.setdata("King Arthur")
FirstClass.setdata(y, 3.14159)
#x.another = "NewValue"
x.display()         # "King Arthur"
y.display()         # 3.14159

z = SecondClass()
z.setdata(42)
z.display()         # 42

'''
from modulename import FirstClass           # Скопировать имя в мою область видимости
class SecondClass(FirstClass):              # Использовать имя класса непосредственно
    def display(self): ...
/////////
import modulename                           # Доступ ко всему модулю целиком
class SecondClass(modulename.FirstClass):   # Указать полное имя
    def display(self): ...
'''

# Another Example
# '''
class Rec():
    pass

def upperName(self):
    return self.name.upper()

Rec.name = 'bob'
Rec.age = 40

x1 = Rec()
y1 = Rec()
x1.name = 'Sue'

Rec.method = upperName

x1.method()     # 'SUE'
y1.method()     # 'BOB'

#print(x.__dict__.keys())
# '''