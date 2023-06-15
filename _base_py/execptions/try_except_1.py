# 1
def one():
    print('How many cats do you have ?')
    numCats = input('Enter: ')

    try:
        if int(numCats) >= 4:
            print('That is a lot of cats.')
        else:
            print('That is not that many cats.')
    except ValueError:
        print('You did not enter a number.')

# one()

# 2
# page 936
def kaboom(x, y):
    print(x + y)

try:
    kaboom([0, 1, 2], 'spam')
except TypeError:
    print('Hello TypeError')
print('resuming here')

# 3
class MyError(Exception): pass

def stuff(file):
    raise MyError()

file = open('data', 'w')
def three(file=file):
    try:
        stuff(file)
    finally:
        file.close()
    print('not reached')

# three()

# 4
# Reapeted execption
def four():
    try:
        raise IndexError('spam')
    except IndexError:
        print('propagating')
        raise

# four()

# 5
def five():
    try:
        1/0
    except Exception as E:
        raise TypeError('Bad!') from E
    # except Exception as Y:
    #     raise IndexError('Index') from Y

five()