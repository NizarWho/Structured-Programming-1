# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:47:54 2022

@author: nza7
"""

# Task 6 - Order System
# 1. ask the user how manu people per table
# 2. ask the user, what each person would like to eat and drink
# . after you ask the user for the number of people
# . Generate uer inputs for each users order
# 3. we want to know the persons name, food order, and drink order
# 4. Print the following for each user at the table 
# 5. Hello, [Name], you ordered [food] with [drink]
# 6. 

orders = []
customers = int(input('How many people will be seated at your table?'))
while customers > 0:
    name, food, drink = input('Hello Customer # {} Enter Your Name, Drink, and Food in a list seperated by spaces'. format(customers)).split()
    orders.append('Hello {} your ordered a {} with a {}'.format(name, food, drink))
    customers -=1 # decrement by 1
print(*orders, sep ='\n')

#Additional Option- if you want to be nice haha
        

orders = []
customers = int(input('How many people will be seated at your table? '))
while customers > 0:
    print('You are customer #, customers ')
    name = input('Hello Customer # {} what is your name? '.format(customers))
    drink = input('Alright {} what would you like to drink? '.format(name))
    food = input('Alright {} what would you like to eat? '.format(name))
    orders.append('Hello {} your ordered a {} with a {} '.format(name, food, drink))
    customers -=1
print(*orders, sep ='\n')
        




