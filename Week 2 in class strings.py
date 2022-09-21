# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:59:10 2022

@author: nza7
"""

#Task 1 - Name Strings

String='Hello'
Print("String") #Incorrect as it will print our the word String
Print('string') #Incorrect as it will print our the word string
print('string') #Case Sensitive
print('String') #Incorrect as wariables are case sens

#Task 2- Combining Strings
string1='Hello'
string2='my name is robot'
string3='#369'
print(string1+string2+string3)

#Fix Spacing issues way #1: adding a ' '  in the command
string1='Hello'
string2='my name is robot'
string3='#369'
print(string1+ ' ' string2+string3)

#or....using a space in the code itself after the '      njkfnskjnfs'
string1='Hello'
string2=' my name is robot'
string3=' #369'
print(string1+string2+string3)

#Combine all cariables an print them on one using big_string
string1='Hello'
string2=' my name is robot'
string3=' #369'
big_string=string1+string2+string3
print(big_string)

#Combine all cariables an print them on one using big_string
string1='Hello'
string2='my name is robot'
string3='#369'
big_string=string1+ ' ' + string2+ ' ' +string3
print(big_string)

#Without using Variables- you may be able to use the simpler one line using print
#this comes with less functionality as you can only use it as one code and can not combine

print('Hello my name is robot #369')

#Task 3- Working with numbers
number1=5       #this is known as an integer Notice there us no ''
float0=5.6       #this is a float as it is a decimal
float1='5.6'    #this is a string as it is a decimal in ''
print(number1)
print(float0)
print (float1)

#option 1 combine into one varibale answer using []

number1=5       #this is known as an integer Notice there us no ''
float0=5.6       #this is a float as it is a decimal
float1='5.6'    #this is a string as it is a decimal in ''
big_number=[number1] + [float0] + [float1]
print(big_number)

#option 2 convert into string using str

number1=5       #this is known as an integer Notice there us no ''
float0=5.6       #this is a float as it is a decimal
float1='5.6'    #this is a string as it is a decimal in ''
big_number=str(number1) + str(float0) + str(float1)
print(big_number) #no bueno

#option 3 you may use 'commas' instead of '+'
 number1=5       #this is known as an integer Notice there us no ''
 float0=5.6       #this is a float as it is a decimal
 float1='5.6'    #this is a string as it is a decimal in ''
 big_number=number1,float0,float1
 print(big_number)
 
#Task 4: recap of task 1 - task 3
string1= 'Hello'
num3=45
print('printing things, woohoo!')
print(23456789)
print(num3)
print(string1)
print(string1, num3)
print(string1, 'I am python number', num3, ',hear me out!')
print(string1 + 'I am python number ' + str(num3) + ', hear me out!')

#Task 5- Solo
#Assign Lebron James to a variable called player_name
#Assign 250 to a variable called player_weight
#print player_name weighs player_weight lbs

player_name1='Lebron James'
player_weight=250
print(player_name1,'weighs', player_weight, 'lbs')


#Task 6- Solo
#set variable phase1 equal to 'Hi everyone'
#set another variable called phase2 equal to 'My name is Nizar Almoughrabi'
#set the 2 variables in a new variable called 'complete' and print

phase1='Hi Everyone'
phase2='My name is Nizar Almoughrabi'
complete= phase1 + ' ' + phase2
print(complete)

#Task 7- Get Specific characters
#1 Assign Hello World to a variable called word
#2 print the 1st char
#3 print the last 2 char
#4 find the total number of char

word='Hello World'
print (word[0:1])
print (word[-2:])
len(word)

#Task 8- working with numbers
#1. use standard symbols like + - * / ** ^
#2. add 3 and 2 and print it
#3. subtract 3 and 2 and print it
#4. divide 3 and 2 and print it
#5. use the ** for 3 and 2 and printit Figure out
#what it is doing
#6. use the ^ on 3 and 2 and print it. figure out
#what it is doing

print(3+2,'Addition')
print(3/2, 'Division')
print(3**2, 'Exponent'), 
print(3^2, 'MODE-returns remainder')

#Task 9 more slicing
#Assign the following string to a varibale called str
#2022-12-09 12:16:40 ABCDEFG
#print DEF09122022

str=('2022-12-09 12:16:40 ABCDEFG')
print(str[23:26] + str[8:10] + str[5:7] + str[0:4])



