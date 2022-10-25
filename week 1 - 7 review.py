# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:39:48 2022

@author: nizar
"""
# Q1. Print a unique List
# Create a list of vals
# vals = cat, dog, cat, bug, dog, ant, dog, bug

vals = ['cat', 'dog', 'cat','bug','dog','ant', 'dog', 'bug']
valsb =set(vals) # this prints the value only 1 time!!
print(*valsb)

# Q2. What will produce the following output
# ['C','r','u','n','c','h','y', 'F','r','o','g']


letters = ['c', 'r', 'u','n','c','h', 'y', 'f', 'r','o', 'g']
print(letters)
    
#or

frog = "Crunchy Frog"
for character_index in frog:
   print(character_index)
   
#or

letters = list(['c', 'r', 'u','n','c','h', 'y', 'f', 'r','o', 'g'])
print(letters) # used data type (list) list to convert a string to a list! 


# Q3. Check if element a is present in the list
# abc=["a", "b", "c", "d", "e"]

abc=test_list=["a", "b", "c", "d", "e"]
x = 'a'
if x in abc:
    print("present")
else:
    print("not present")
    
#or

abc=["a", "b", "c", "d", "e"]
if 'a' in abc:
    print('yes')
else:
    print('no')

#or
abc=["a", "b", "c", "d", "e"]
print(abc.index('a'))

#or
abc=["a", "b", "c", "d", "e"]
print(abc.count('a'))

# Q4. str="Python under Linux is great"
# print every 3rd Character

str="Python under Linux is great"
print(str[::3])

# Q5. Write a Python program that prompts the user for two numbers, reads 
# them in, and prints out the product, labeled.

 a = int(input('Pick a number: '))
 b = int(input('Pick another number: '))
 print('The product of the number are:  ', a*b) 
 
 #or
 
 a = int(input('Pick a number: '))
 b = int(input('Pick another number: '))
 c = a*b
 print('The product of the number are:  ', c) 

# Q6. Suppose you know x is an interger and ys is a string representing an 
# interger, For instance, x is 3 and ys is '24'. Write code to print out the 
# arithmetic sum of the two. In this example case, 27 would be printed.

x = 3
ys = int('24')
print(x + ys)

# Q7. Print all positive numbers from the list
# [3, -5, 2, -1, 0, 7]

num = [3, -5, 2, -1, 0, 7]
for i in num:
    if i > 0:
        print(i)

# Q8. Make up a list of 5 colors and
# - Print all the items in the list.
# - Print a message for each item
# - Print a standard message afterwards

colors = ['blue', 'green', 'yellow', 'red']
print (*colors)
for i in colors:
    print('this is the color of my pants', i)
print('thank you for your input!')

#or use a while loop- useing i =0, len, and i +=1

colors = ['blue', 'green', 'yellow', 'red']
print (*colors)
i = 0
while i < len(colors):
    print('this is the color of my pants', i)
    i += 1
print('thank you for your input!')

# Q9. Using the list created above and print "We have ____ colors. Where the 
# ______ represents the total number of colors

colors = ['blue', 'green', 'yellow', 'red']
num_colors = len(colors)
print('we have', num_colors, 'colors. Where the', num_colors, 'represents the total number of colors')

# Q10. Complete the code below:
# # Select the first list element
# oneZooAnimal = biggerZoo[0]
# # Print "oneZooAnimal"
# print(_____________)

biggerZoo = ['Lion','Tiger','Bear']
oneZooAnimal = biggerZoo[0]
print(oneZooAnimal)

