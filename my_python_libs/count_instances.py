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

if __name__ == "__main__":
    x = Spam()
    x1, y1 = Sub(), Sub()
    x2, y2, z2 = Other(), Other(), Other()

    print(x.numInstances, y1.numInstances, x2.numInstances)