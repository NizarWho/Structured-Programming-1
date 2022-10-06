# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:29:13 2022

@author: nza7
"""

# Decison Making in pythong, If/else/elseif
# multiple conistions not neseted ifs

var = 100 
if (var == 100) : print ("Value of expression is 100")
print ("Good bye!") 

# elif - what should happen if nothing is met
# IF - if your condition TRUE value this will happen
# Else - This will happen if False value
# example 1:
var1= input
if var1 == 100:
    print('true!')
elif var1:
        print('elif')
    else:
        print('nothing')
print('byebye')

#example 2
var = 100 
if var == 200: 
   print ("1 - Got a true expression value" )
   print (var) 
elif var == 150: 
   print ("2 - Got a true expression value" )
   print (var) 
elif var == 100: 
   print ("3 - Got a true expression value" )
   print (var) 
else: 
   print ("4 - Got a false expression value") 
   print (var) 
 
print ("Good bye!") 

# nested loops Syntax
#f expression1: 
 #  statement(s) 
   #if expression2: 
    #  statement(s) 
  #elif expression3: 
   #   statement(s) 
   #else: 
    #  statement(s) 
   #elif expression4: 
    #  statement(s) 
#else: 
   #statement(s) 
   
# Examlpe 1:
var = 100 
if var < 200: 
   print ("Expression value is less than 200" )
   if var == 150: 
      print ("Which is 150") 
   elif var == 100: 
      print ("Which is 100" )
   elif var == 50: 
      print ("Which is 50") 
   elif var < 50: 
      print ("Expression value is less than 50" )
else: 
   print ("Could not find true expression" )
 
print ("Good bye!" )
 
    elif var == 50: 
      print ("Which is 50" )
   elif var < 50: 
      print ("Expression value is less than 50" )
else: 
   print ("Could not find true expression" )
 
