# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:01:50 2022

@author: nizar
"""

# Enhance the given code/ I changed the variabele names to make it unique!

print('\n Welcome to Rutgers Newark Virtual Tour! What would you like to do?')
def virtualtour ():
    choice =''
    while choice !='q':
        print('\n [1] Enter #1 to go for a campus tour.')
        print('\n [2] Enter #2 to go meet the professors.')
        print('\n [3] Enter #3 to listen to a lecture.')
        print('\n [4] Enter #4 to take a break.')
        print('\n [q] Enter #the letter q to quit the tour.')
        choice = input('\n What would you like to do?')
        if choice == '1':
            print('\n Alright, we will start byb looking at Blumenthal Hall! \n')
        elif choice == '2':
            print('\n We will first meet professor Mirchandani- the legend 😎 \n')
        elif choice == '3':
            print('\n We will be listeing to a lecture given at the business school for a CNA class! Prof. X \n')
        elif choice == '4':
            print('\n Bathrooms are upstairs and gift shop is downn the hall, we can circle back in 15 minutes! \n')
        elif choice == 'q':
            print('\n [y] yes \n')
            print('\n [n] no \n')
            toquit=input('\n Are you sure you want to quit this tour? [y] yes \n [n] no \n')
            if toquit =='n':
                virtualtour()
            elif toquit == 'y':
                    break
        else:
            print('Invalid Input, please type y for yes and n for no') 
        virtualtour()
        print('Thank for joining our virtual campuis tour, see you later!')
        
# Favorite colors
def favoritecolors():
    for name in ['James', 'Nizar', 'Zack']:
        print('Hello', name)
        color=input(' \n Type your favorite color: ')
        print(name, 'your favorite color is:', color, '.')
    return;
favoritecolors()

# Phones 
def phones():
    for model in ['Samsung Galaxy S22 Ultra', 'Apple iPhone 14 Pro Max', 'Google Pixel 7 Pro']:
        print('\n The', model, 'is a great choice')
        os = input('\n What is the Operating System? \n')
        print('\n Your Preferance: \n', model, os)
    return;
phones()



# Accepting a sequence of arbitrary length
def numsum (*arguments):
    total = 0
    for numbers in arguments:
        total += numbers
    print('The total sum is:', total)
    return;
numsum(5, 10, 15, 20)





