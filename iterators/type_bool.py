flag = False

N = int(input('Enter number of tryes: '))

for i in range(N):
    x = int(input('Enter number: '))
    flag = (x == 0) or flag

print(flag)