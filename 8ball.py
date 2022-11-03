# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:16:37 2022

@author: nza7
"""
# 8 Ball Program Creation

# Phase 1 # Prereq
# 1. Created .txt fil within same folder .py
# 2. Enetered one statemtn per line in .txt file
# 3. Ask user questions
# 4. After ENTER- display random statement from .txt
# Functions that you may use:
    #file object, random, dictionary, for, input

import random
magicball={}
counter = 0

# import 8ball.txt file
# Build dict. with all possibilities

file = open('8ball.txt')
for line in file:
    magicball.update({counter: line.split('\n')[0]})
    counter += 1
print('Seeing into', counter, 'possible futures.')
input('Ask the magic 8 Ball a question: ')
answerkey = random.randrange(counter)
print('')
print(magicball[answerkey])




