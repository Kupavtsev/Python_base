class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):               # Крайний случай для итераций
        print(f'get[{i}]:', end='')         # А также для индексирования и срезов
        return self.data[i]
    def __iter__(self):                     # Предпочтительный для итерация
        print('iter=> ', end='')            # Возможен только 1 активный итератор
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data

X = Iters([1, 2, 3, 4, 5])
print(2 in X)
for i in X:
    print(i, end=' | ')

print()
print([i **2 for i in X])       # Другие итерационные контексты
print(list(map(bin, X)))
I = iter(X)
while True:
    try:
        print(next(I), end=' @ ')
    except StopIteration:
        break



'''
# 1
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

if __name__ == '__main__':
    for i in Squares(1, 5):
        print(i, end=' ')
'''