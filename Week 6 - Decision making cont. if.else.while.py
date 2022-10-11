# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:38:11 2022

@author: nza7
"""

#Chapter 7/8 ifs, loops etc.

# Task 1: Ask the user for an input and print it
# Hint input
name=input('what is your name?')
print('your name is', name)

# Task 2- enhancing task 1- 
# Keep asking the same question over and over again
# Hint: Input, While
name=input('what is your name?')
while name == name:
    print('your name is', name)
    
# OR!!! you can do it this way: this asks the qustion over and over again
# INFINITE LOOP
while True:
    name=input('what is your name?')
    print('your name is', name)

# Task 3- Enhancing task 2, combine if, loop and input
# 1. Ask the user to guess your secret word
# 2. if the user guesses correctly reply- break the loop
# 3. if the user guesses incorrectly ask the question again
# Hint: input, while, if, break
while True:
    word=input('what is the secret word?')
    if word == 'jelly':
        print('You got it, the secret word is jelly')
        break
    else:
        print('try again')
    
# attempt 2:
    
    while True:
        guess= input('What is the secret word?')
        if guess=='jelly':
            print('good job! you got it!')
            break
  
# Task 4- 
# 1. Ask the user to guess your number
# 2. if the guessed number is higher than your number print 'lower'!
# 3. if the guessed number is lower print higher!
# 4. if it is correct print correct

while True:
    number_a=int(input('Guess the number!'))
    if number_a == 21:
        print('correct!')
        break
    elif number_a > 21:
        print('Lower!!')
    elif number_a < 21:
        print('Higher!')


#option number 2- uses else

y = 26
x = ' '
while (x != y):
    x=int(input('guess any number:'))
    if x > y:
        print('Lower!')
    elif x < y:
        print('Higher!')
    else:
        print('Correct!')

# Task 5-
# Enhance task 4 but printing number of tries
# print correct in [num] of tries 
# correct in x tries
        
y = 26
x = ' '
z = 0
while (x != y):
    z+=1
    x=int(input('guess any number:'))
    if x > y:
        print('Lower!')
    elif x < y:
        print('Higher!')
    else:
        print('Correct! It toke you', z, 'attempt/s')
    

        






