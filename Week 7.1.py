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
    
    
# 11/01/2022- week 8 updates
# Task 3 - change it to a function

def askfeeling(): # defined the funtioned and name() if need inputs you can ut them in parenthesiss and seperate with comma 
    print('How are you feeling?')
    feeling = input()
    print ('I am happy to hear that you are feeling', feelings)
    return;
print('Good Morning')  # we are doing a function call 3 times! 3 diffrent messages we have 
askfeeling()
print('Good Morning')
askfeeling()
print('Good Morning')
askfeeling()

# Task 3.1 repeat the same as 3 but, use a loop this time!

def askfeeling(): # defined the funtioned and name() if need inputs you can ut them in parenthesiss and seperate with comma 
    print('How are you feeling?')
    feeling = input()
    print ('I am happy to hear that you are feeling', feelings)
    return;
for timeofday in ['Good Morning', 'Good Afternoon', 'Good Evening']:
    print(timeofday)
    print('How are you feeling?')
    feeling = input()
    print('I am happy to hear that you are feeling', feeling)

# or put the foor loop inside!!

def askfeeling():
    for timeofday in ['Good Morning', 'Good Afternoon', 'Good Evening']:
        print(timeofday)
        print('How are you feeling?')
        feeling = input()
        print('I am happy to hear that you are feeling', feeling)
        # return; do not use return! we do not want to close the function
askfeeling()


