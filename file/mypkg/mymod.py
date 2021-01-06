# Task for import

def countLines(name):
    file = open(name)
    result = len(file.readlines())
    print(result)
    return len(file.readlines())

def countChars(name):
    file = len(open(name).read())
    print(file)
    return file

def test(name):
    countLines(name)
    countChars(name)

if __name__ == '__main__':
    test('myfile.txt')