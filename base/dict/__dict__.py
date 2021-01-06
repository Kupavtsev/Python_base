class Scalping(object):
    def __init__(self):
        self.open = 50
        self.close = 100

s = Scalping()
print(s.__dict__)
print(dir(s))