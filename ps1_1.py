# Problem Set 1

'''Assume s is a string of lower case characters.

Write a program that counts up the number of vowels 
contained in the string s. Valid vowels are: 
'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:


Number of vowels: 5'''

s = 'azcbobobegghakl'
vowels = 'aeiou'
da_string = ''

for letter in s:
    if letter in vowels:
        da_string = da_string + letter

print("Number of vowels: " + str(len(da_string)))


'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print:

Number of times bob occurs is: 2'''

s = 'azcbobobegghakl'
bob = 'bob'
x = 0
y = 3
counter = 0
for letter in s:
    while y < len(s):

        possible_bob = s[x:y]
        x += 1
        y += 1
        if possible_bob == bob:
            counter = counter + 1

print(counter)
