# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:50:25 2022

@author: nza7
"""

# For
computer_brands = ['Apple','Asus', 'Dell', 'Samsung']
for brands in computer_brands:
        print(brands)
        
# While 

computer_brands = ['Apple','Asus', 'Dell', 'Samsung']
i = 0
while i < len(computer_brands):
    print(computer_brands[i])
    i = i + 1
    
# While True

while True: 
    answer = input("Start typing...") 
    if answer == "quit": 
        break 
    print ("Your answer was", answer)
 
# While Counter

counter = 0 
while counter <= 100: 
    print (counter)
    counter +=2 # counter = counter + 2
    
#Infinite True
 
while True: 
    print ("Hello World")
    
# Nesting Loops

for x in range(1, 11): 
    for y in range(1, 11): 
        print ('%d * %d = %d' % (x, y, x*y)) # same as the line below just difreent way of writting
        print (x, '*', y, '=', x*y ) # avoids variable string, variable string

# Nesting Loop 2

 
name = 'marcog' 
number = 42 
print ('%s %d' % (name, number))
 
# or

print (name, str(number))





