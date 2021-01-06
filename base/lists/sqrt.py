#Functions task 9
import math

L = [2, 4, 9, 16, 25]

#1
for x in L:
    print(math.sqrt(x))

#2
t = (map(math.sqrt, L))
r = map((lambda x: math.sqrt(x)), L)
print(list(r))

#3
b = [math.sqrt(x) for x in L]
print(list(b))