# Task for import

def countLines(file):
    file.seek(0)
    print(len(file.readlines()))
    return len(file.readlines())

def countChars(file):
    file.seek(0)
    print(len(file.read()))
    return len(file.read())

def test(name):
    file = open(name)
    countLines(file)
    countChars(file)

if __name__ == '__main__':
    test('myfile.txt')