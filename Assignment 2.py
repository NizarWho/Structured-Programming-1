# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:12:09 2022

@author: nza7
"""

# First List- Loop
colors = ['yellow', 'red', 'blue', 'green', 'black']
for x in range(len(colors)):
    print (colors[x])

# First Neat List- Loop
colors = ['yellow', 'blue', 'white', 'black']
clothing = ['shirt', 'shoe', 'pants', 'hat']
y = 0
for x in colors:
    print(x, 'is a great color', clothing[y])
    y+=1
    
#Your first list - Loop
colors = ['yellow is a great color hat', 'red is a great colors show', 'blue is a great color dress', 'green is a great color belt', 'black is a great color coat']
for x in range(len(colors)):
    print (colors[x])
   
    
# or...
colors = ['yellow', 'blue', 'white', 'black']
clothing = ['shirt', 'shoe', 'pants', 'hat']
y = 0
for x in range(len(colors)):
    print (colors[x], 'is a great color for your', clothing[y])
    y+=1
    
    
#Exercise: Working List
careers= ['Teacher', 'Dr', 'Engineer']
for x in careers:
    print(careers[0])
careers.append('chef')
print(careers)
careers.insert(0, 'PM')
print(careers)
for x in range(len(careers)):
    print (careers[x])
    
# Starting from empty
list1=[]
list1.append('PM')
list1.append('Teacher')
list1.append('Dr')
list1.append('Engineer')
list1.append('Chef')
print(list1)
print(list1[0], 'is a project manager- it is hefty work!')
print(list1[4], 'is a fun career that revolves around art')

# Ordered Working List
careers= ['Teacher', 'Dr', 'Engineer']
print(*careers, 'Orignial')
for i in careers:
   print(sorted(careers), '-Alphabetical') 
   print(careers, '-Original')
   print(sorted(careers, reverse=True), '-Reverse')
   print(careers, '-Original')
   careers.reverse()
   print(careers, '-Reverse')
   careers.remove('Teacher')
   careers.remove('Engineer')
   careers.insert(1, 'Engineer')
   careers.insert(2, 'Teacher')
   print(careers, '-Alphabetical')
   careers.remove('Dr')
   careers.remove('Engineer')
   careers.insert(1, 'Engineer')
   careers.insert(2, 'Dr')
   print(careers, '-Reverse')
   break

# Ordered Numbers
num=[0,1,2,3,4]
print(num, '-Original')
for i in num:
    print(sorted(num), '-Increasing') 
    print(num, '-Orginal')
    print(sorted(num, reverse=True), '-Decreasing')
    print(num, '-Original')
    num.reverse()
    print(num, '-Reverse')
    num.reverse()
    print(sorted(num), '-Original')
    print(num, '-Increasing')
    print(sorted(num, reverse=True), '-Decreasing')
    break


# List Lengths
colors = ['yellow', 'red', 'blue', 'green', 'black']
print(*colors, '\n this list is =', len(colors),'units long')
careers= ['Teacher', 'Dr', 'Engineer']
print(*careers, '\n this list is =', len(careers),'units long')
