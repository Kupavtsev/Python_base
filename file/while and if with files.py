file = open('test.txt', 'rb')
# print(file.read())

'''
file = open('test.txt')

while True:
    char = file.read(1)
    if not char: break
    print(char, end='')
        
for char in open('test.txt').read():
    print(char, end='')
'''

while True:
    line = file.readline()
    if not line: break
    print(line, end='')

while True:
    chunk = file.read(10)
    if not chunk: break
    print(chunk)

for line in open('test.txt'):
    print(line, end='')
