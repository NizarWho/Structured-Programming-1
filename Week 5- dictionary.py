# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:42:23 2022

@author: nza7
"""
# Practicing Variables in Dictionaries

#Task 3 - Ceate a dictionary about pets
# 1. Each value pair has the name and the type of animal
# 2. Print the name and the type of animal as belo
# [Animal] is a [type]
# Example: Ziggy is a Canary
# Hint: for loop and dictionary []

# Used Zip to assicated the keys to the values
dict = {}
dict ['Charlie'] = 'is a doggy'
dict ['Moon'] = 'is a Kitty'
dict ['Aqua'] = 'is a Fishy'
dict ['Rave'] = 'is a Birdy'

for x,y in zip(dict.keys(), dict.values()):
    print(x,y)
    
# option 2: make one large dictionary using zip
dict={'Charlie': 'is a doggy', 'Moon': 'is a kitty', 'Aqua': 'is a fishy', 'Rave': 'is a birdy'}
for x,y in zip(dict.keys(), dict.values()):
    print(x,y)
    
# option 3: does not work, the only way to do this key and values in dict is to use zip
dict={'Charlie': 'doggy', 'Moon': 'kitty', 'Aqua': 'fishy', 'Rave': 'birdy'}
for x,y in range(len(dict)):
    print(dict.keys(x), 'is a', dict.values(y))
