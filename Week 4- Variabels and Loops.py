# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = b = c = 1
a = 1
b = 1
c = 1
 

a,b,c = 1 [2,3], 'hello'
a = 1
b = 1
c = 1


# Combine concepts of loops and lists
# Task 1 -  Traverse through 2 or more lists
# 1. Create a list of names in one sequence
# 2. Create a list of hobbies in another sequence called hobbies
#    for the corresponding person in name
# 3. Print [Name] love [hobby]
# 4. Example: Alice loves hacking
# Hint: for loop


# attempt 1
name = ['Nizar', 'Jona', 'Ang', 'Reed']
hobbies = ['reading', 'coding', 'swimming', 'wood working ']
for x in range(len(hobbies)): # x is every element in the list # Len is going to pull out coresp values and print for every element
    print (name[x], 'Loves', hobbies[x])

# attempt 2
name = ['Nizar', 'Jona', 'Ang', 'Reed']
hobbies = ['reading', 'coding', 'swimming', 'wood working ']
y = 0 # initialize at 0
for x in name:
    print(x, 'loves', hobbies[y])
    y+=1 # this increments by one, no using len or range
    
# attempt 3
name = ['Nizar', 'Jona', 'Ang', 'Reed']
hobbies = ['reading', 'coding', 'swimming', 'wood working ']
for name, hobbies in zip(name, hobbies): # zip goes over the entire list until end of the last element of the shortest list shortest list
    print(name, 'loves', hobbies)

# Task 2 - enhance task1
# 1. add age in a new list called age
# 2. print their name, hobby, and age
#    [name] is [age] years old and his/her hobby is [hobby]
# Example: Nizar is 21 years old and his/her hobby is reading

# option 1: use range and len
name = ['Nizar', 'Jona', 'Ang', 'Reed']
hobbies = ['reading', 'coding', 'swimming', 'wood working ']
age = ['21', '19', '36', '53']

for x in range(len(hobbies)):
    print (name[x], 'is', age[x], 'years old and his/her hobby is', hobbies[x])
    
# option 2: initalize using y and z 
name = ['Nizar', 'Jona', 'Ang', 'Reed']
hobbies = ['reading', 'coding', 'swimming', 'wood working ']
age = ['21', '19', '36', '53']
y = 0
z = 0

for x in name:
    print (x, 'is', age[y], 'years old and his/her hobby is', hobbies[z])
    y+=1
    z+=1
    
# option 3: use zip
name = ['Nizar', 'Jona', 'Ang', 'Reed']
hobbies = ['reading', 'coding', 'swimming', 'wood working ']
age = ['21', '19', '36', '53']

for name, age, hobbies in zip(name, age, hobbies):
    print (name, 'is', age, 'years old and his/her hobby is', hobbies)
    



