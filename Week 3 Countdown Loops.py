# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 12:24:15 2022

@author: nza7
"""

# Week 3
# TASK 1
# Create a countdown
# Output should be
# 10
# 9
# 8
# 7
# 6 ...
# 0
# USE WHILE LOOP

countdown = 10 # start with counting from ten 
while countdown >= 0:  # numbers stop at 0 and range from 0-10
    print (countdown)  # print the string
    countdown -= 1     # use the decrements of -1 eveyrtime
    
# Task 2- Enhance task 1 
# Print Blastoff! instead of 0
    
counter=10
while counter >=0:
    print(counter)
    counter -=1
    if counter==0:
        print("Blastoff!")
        break
#OR

counter=10
while counter >=1:
    print(counter)
    counter -=1
print("Blastoff!")

#OR

counter=10
while counter >=1:
    print(counter)
    counter -=1
    if counter==0:
        print("Blastoff!")
    