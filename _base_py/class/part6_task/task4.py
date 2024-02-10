class Meta:
    def __init__(self, data=None) -> None:
        self.test = data
    def __getattr__(self, atr):
        print('attribute...')
        if atr == 'name':
            return 555
        else:
            raise SyntaxError

exp = Meta(1)
print(exp.name)