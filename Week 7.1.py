# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:45:49 2022

@author: nza7
"""

# Task 1 - Print Statements
# 1. Print 'Good Morning'
# 2. Print 'How are you feeling?'
# 3. Ask the user for their input
# 4. Print the statment 'I am happy to hear that you are
#    feeling', [Feeling]

print('Good Morning!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling', feeling)
print('I am happy to hear that you are feeling' + feeling)

# Repeat for Good Afternoon- very simple tweak

print('Good Afternoon!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling', feeling)
print('I am happy to hear that you are feeling' + feeling)

# Repeat for Good Evening- very simple tweak

print('Good Evening!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling', feeling)
print('I am happy to hear that you are feeling' + feeling)

# Task 2 - Change task 1 to a loop
good = ['Good Morning', 'Good Afternoon', 'Good Evening']
while True:
        print(input('What time of day is it?'))
    if input == 'morning':
        print(good(0))
    else if input == 'afternoon':
        print (good(1)
    else if input == ('evening'):
        print (good(2))
        
# Attempt 2:

timeofday= ['Good Morning', 'Good Afternoon', 'Good Evening']
for x in timeofday:
    print(x)
    print('How are you feeling?')
    feeling = input()
    print('I am happy to hear that you are feeling', feeling)

# Attempt 3:

for timeofday in ['Good Morning', 'Good Afternoon', 'Good Evening']:
    print(timeofday)
    print('How are you feeling?')
    feeling = input()
    print('I am happy to hear that you are feeling', feeling)
