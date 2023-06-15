class Task4:
    def __getitem__(self, i):
        return self.pset[i]

a = Task4()
b = Task4()

a.pset = {1,2,3}
b.pset = {5,6,7,3}

print(a.pset[1])