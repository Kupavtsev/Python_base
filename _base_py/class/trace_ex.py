class Wrapper:
    def __init__(self, object) -> None:
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Trace: ', attrname)          
        return getattr(self.wrapped, attrname)          # Делегировать извлечение

if __name__ == '__main__':
    x = Wrapper([1,2,3])
    x.append(4)
    print(x.wrapped)        # [1, 2, 3, 4]

    y = Wrapper({'a': 1, 'b': 2})
    print(y.keys())         # dict_keys(['a', 'b'])