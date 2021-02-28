# Functions task 8

def factor(y):
    if y <= 1:
        print(y, 'not prime')
    else:
        x = y // 2
        while x > 1:
            if y % x == 0:
                print(y, 'has factor', x)
                break
            x = x - 1
        else:
            print(y, 'is prime')

    
factor(-20)
factor(13)
factor(13.0)
factor(15)
factor(15.0)
    