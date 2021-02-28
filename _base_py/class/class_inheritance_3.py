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
a.display()
print(a)
b = a + 'xyz'
print(b)
a.mul(3)
print(a)
    

x = FirstClass()
y = FirstClass()

x.setdata("King Arthur")
FirstClass.setdata(y, 3.14159)
#x.another = "NewValue"
x.display()
y.display()

z = SecondClass()
z.setdata(42)
z.display()

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
'''
class rec: pass

def upperName(self):
    return self.name.upper()

rec.name = 'bob'
rec.age = 40

x = rec()
y = rec()
x.name = 'Sue'

rec.method = upperName

x.method()
y.method()

#print(x.__dict__.keys())
'''