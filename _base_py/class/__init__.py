class Some(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def newClassInst(**kwargs):
    self = Some(**kwargs)
    return self

k = newClassInst(a = 100, b = 'string', c = {'1': 12, '2': 32})

print(k.a)
print(k.b)
print(k.c)