'''
import mymod

def test(name):
        mymod.countLines(name)
        mymod.countChars(name)

if __name__ == '__main__':
    test('myfile.txt')

'''

#2
from mymod import *

def test2(name):
        countLines(name)
        countChars(name)

if __name__ == '__main__':
    test2('myfile.txt')