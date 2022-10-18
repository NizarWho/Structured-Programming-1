# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:43:42 2022

@author: nza7
"""

# Task 7 - Wage Calculation
# 1. Ask the user for their number of hours worked and their hourly wage
# 2. If they work 40 hours (or less) multiply their wage by the hours. 
# 3. For each additional hour worked they should get 1.5x their wage
# 4. Print you made  $[wages] for the hours ([hours]) worked
# Example: you made $20 for the hours (2) worked.
# HINT: if, placeholders, int/float

hworked = int(input('How many hours have you worked? ')) #took input from user
wages = float(input('How much do you make an hour? '))
if hworked <= 40:
    salary = hworked * wages
else:
    ohours = hworked * 40
    salary = (40 * wages) + (ohours * wages * 1.5)
print ('You made {} for the hours ({}) worked.' .format (salary, hworked))


# Task 8 - Choices
# 1. Print a welcome message
# 2. Give the user 5 choices. If a user selects (types) a number (choice) then 
# show them the message corresponding to the number typed
# 3. Keep askinf them for their choice until they type q
# Hint: while, if, elif, else

welcome= (input('Welcome user!! Pleased to have you join us today!'))
types =(input('Chose on of the types: {1}number, {2}Letter, {3} word, {4}q, {5}character'))
while True:
    print(welcome + types)
    if types =int(1):
        print ('You have chosen a number!')


# Attempt 2:
print(input(' Welcome, chose one of the 5 options! \n Enter a number between 1 and 5 to find out what message you recieve...\n if you want to quit enter q \n ENTER HERE: '))        
option1='You are cool 😎'
option2='I like pop tarts'
option3='I <3 Matt Bellamy'
option4='Listen to Gojira if you like metal'
option5=''
while option != 'q':
    options = input('Your number:')
    if options == '1':
        print(option1)
    elif options == '2':
        print(option2)
    elif options == '3':
        print(option3)
    elif options == '4':
        print(option4)
    elif options == '5':
        print(option5)
    else:
        print('Invalid Choice, chose from 1-5!')
        
        
# Attempt 3:
print(input(' Welcome, chose one of the 5 options! \n Enter a number between 1 and 5 to find out what message you recieve...\n if you want to quit enter q \n ENTER HERE: '))        
option1='You are cool 😎'
option2='I like pop tarts'
option3='I <3 Matt Bellamy'
option4='Listen to Gojira if you like metal'
option5=''
while true:
    options = input('Your number:')
    if options == '1':
        print(option1)
    elif options == '2':
        print(option2)
    elif options == '3':
        print(option3)
    elif options == '4':
        print(option4)
    elif options == '5':
        print(option5)
    elif options == 'q'
    break
    else:
        print('Invalid Choice, chose from 1-5!')
        
#OPTION1
print("Welcome, There are 5 options to choose from.\nEnter a number between 1 and 5
to find what message you receive...\nIf you want to Quit enter q")
option1="Have a great day."
option2="It will rain."
option3="Charge your Phone."
option4="Find a cool rock"
option5="Go get some icecream"
options=""
while options !="q":
    options=input("Your Number: ")
    if options=="1":
        print(option1)
    elif options=="2":
        print(option2)
    elif options=="32":
        print(option3)
    elif options=="4":
        print(option4)
    elif options=="5":
        print(option5)
    else:
        print("Invalid Choice")
#OPTION2
print("Welcome, There are 5 options to choose from.\nEnter a number between 1 and 5 to find what message you receive...\nIf you want to Quit enter q")
option1="Have a great day."
option2="It will rain."
option3="Charge your Phone."
option4="Find a cool rock"
option5="Go get some icecream"
while True:
    options=input("Your Number: ")
    if options=="1":
        print(option1)
    elif options=="2":
        print(option2)
    elif options=="3":
        print(option3)
    elif options=="4":
        print(option4)
    elif options=="5":
        print(option5)
    elif options=="q":
        print("Bye") 
        break
    else:
        print("Invalid Choice")