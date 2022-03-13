base = 7
x = int(input('eneter number: '))
while x > 0:
    digit = x % base
    print(digit, '\n')
    x //= base