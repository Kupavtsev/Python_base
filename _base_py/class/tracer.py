class Decorator:
    def __init__(self, func) -> None:
        self.calls = 0
        self.func = func
    def __call__(self, *args: any) -> any:
        self.func(*args)
        self.calls += 1
        print('Call: ', self.calls)

@Decorator
def tracer(a,b,c):
    print(a,b,c)

tracer(1,2,3)
tracer(20,442,73)
tracer(1,'afaf',3)