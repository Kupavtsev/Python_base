# input / list / for if / range
# list / append / slice // dict / for if / range
# list / replace / slice = replace


#   ---> 1 <--- copy of list
# input / list / for if / range

# Here is the amount of values in list
N = int(input())
A = [0] * N
B = [0] * N

for value in range(N):
    # putting values one by one to the list A
    A[value] = int(input())
for value in range(N):
    # Copy all values from list A to list B
    B[value] = A[value]

print(A, B)

#   ---> 2 <--- Create dict in range and append it to list
# list / append / slice // dict / for if / range

aliens = [] # create empty list

for alien_num in range(100):
    new_alien = {}  # create empty dict
    new_alien['color'] = 'green'
    new_alien['points'] = 5
    new_alien['x'] = 20 * alien_num
    new_alien['y'] = 0
    # in one loop we have one dict
    aliens.append(new_alien) # add this dict to the list

num_aliens = len(aliens)

print(aliens[20:40]) # slice a part of list elements
print("Number of aliens created:")
print(num_aliens)


#   ---> 3 <--- 
# list / replace / slice = replace

spam = [10,20,30]
spam[1] = 'Hello'                   #Replace [10, 'Hello', 30]
spam[1:3] = ['CAT', 'DOG', 'MOUSE'] #Slice - with replace [10, 'CAT', 'DOG', 'MOUSE']
print(spam)