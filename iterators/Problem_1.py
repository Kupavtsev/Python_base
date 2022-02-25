#Write a program that counts up the number of vowels contained
#in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

s = 'azcbobobegghakl'
vowels = 0

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        vowels += 1
print('Number of vowels: ' + str(vowels))        


# Another app

z = 'azcbobobegghakl'
product = 'bob'
vowels2 = 0

for letter in range(len(z)):
    if z[letter] in product:
        vowels2 += 1
print('Number of vowels: ' + str(vowels2))  