# import sys

# task #2
class MyList(object):
    def __init__(self, data=None):
        print('INIT')
        self.data = data[:]
    def __add__(self, other):
        print('ADD')
        self.data = self.data + other
    def __getitem__(self, i):
        print('__getitem__')
        return self.data[i]
    def __iter__(self):
        # print('__iter__')
        self.ix = 0
        return self
    def __next__(self):
        # print('__next__')
        if self.ix == len(self.data): raise StopIteration
        else:
            item = self.data[self.ix]
            self.ix += 1
            return item

  
# m1 = MyList([1,2,3,5,6])
# x = [x**2 for x in m1]
# print(x)

# Task3
class MyListSub(MyList):
    insCount = 0
    clsCount = 0
    def __init__(self, data=None):
        self.data = data
    def __add__(self, other):
        self.count()
        MyListSub.clsCounter()
        super().__add__(other)
        print(self.insCount)
    def count(self):
        self.insCount += 1
    @classmethod
    def clsCounter(cls):
        cls.clsCount += 1

a = MyListSub(11)
a + 100
print(a.data)
a.c = a + 200
print(a.c)
b = MyListSub(22)
b + 1000
print(b.data)
print(MyListSub.clsCount)
print(MyListSub.__bases__)