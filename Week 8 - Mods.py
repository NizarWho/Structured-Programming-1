# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:32:52 2022

@author: nza7
"""
# We have used this in week 5 loops
# we will add mods!!
import math, random

y=math.floor(random.random()*100)+1
x=""
z=0
while (x !=y):
    z+=1
    x=int(input("Guess my number: "))
    if x > y:
        print("Lower!")
    elif x < y:
        print("Higher!")
    else:
        print("Correct in", z,"tries")
        
# Task - Random Number Generator mods!

#checking what math and random mod contain
import math, random
print(dir(math))
print(dir(random))

y=math.floor(random.random()*100)+1
x=""
z=0
while (x !=y):
    z+=1
    x=int(input("Guess my number: "))
    if x > y:
        print("Lower!")
    elif x < y:
        print("Higher!")
    else:
        print("Correct in", z,"tries")
        