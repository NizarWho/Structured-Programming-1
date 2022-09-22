# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:55:06 2022

@author: nza7
"""

#Task 1- Sorting Lists
#Assign the following values to a list called cars-used L instead
#BMW, Audi, Toyota, Honda, Subaru
#Print the original list
#Print the list sorted alphabetically (Ascending)
#Print decending
#Re-print the orginal list
#Print the list with the values reversed

L =['BMW', 'Audi', 'Toyota', 'Honda', 'Subaru']
print(L)
print(sorted(L))
print(sorted(L, reverse=False))
print(sorted(L, reverse=True))
print(L)
L.reverse()
print(L)
# Used Sorted not l.sort assorted. This keeps the orignial
#list and l.sort changes the orginal list

#Task 2-more lists
#Assign the following to a list called motorcycle
#Harley, Honda, Yamaha, Suzuki, Ducati
#Assin Ducati to a variable called too_expensive
#Remove the too_expensive for the too_expensive bike
#[bike name] is too expensive for me
#Where [bike name] is the value of the too_expensive bike
#Print with title case

mc= ['harley', 'honda', 'yamaha', 'suzuki', 'ducati']
too_expensive='ducati'
print(mc)
mc.remove(too_expensive)
print(too_expensive.title(), 'is too expensive for me!')
print(mc)

#Task 3- Slicing Lists
#Create a list called colors and assing the values
#yellow, red, blue, green, black
#print black and yellow from the list
#print yellow and green from the list 
#put a space between the values- concat or ,

colors = ['yellow', 'red', 'blue', 'green', 'black']
print(colors[4], colors[0])
print(colors[-1], colors[0])
print(colors[0], colors[3])
print(colors[0] + ' ' + colors[3])





