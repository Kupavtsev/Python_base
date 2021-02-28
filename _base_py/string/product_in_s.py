s = 'azcbobobegghakl'
product = 'bob'
vowels = 0
index = 0
i = 0

while index < len(s):
    for letter in s:
        if s[index] == 'b':
            vowels += 1
        index += 1

while product in s and i < 4:
    print(product)
    i += 1

        
print('Number of vowels: ' + str(vowels))        
