#Task 3- Ask user for input
from pickletools import int4

name =input('What is your name? ')
print(name)

#OR

name = input('What is your name? ')
print('Your name is ', name.title())

#or you can combine the two

print(input('Your name is ', name))

#Task 4-enhance task 3 using loops
#1. ask the same question over and over again until the user types 'q'
#2. if the user types q- break the loop
#3. Print the user response
# Hint: while, if, break, print

while True: 
    name = input("What is your name? ") 
    if name == "q": 
        break 
    print('Your name is ', name.title())

#Task 5- more input
#1. Ask the user for hours worked
#2. Take the users input and multiply it by 10
# Print based on the usreers numbers of hours worked , you earned $___
 
#attempt 1
hours = input("How many hours did you work? ")
print('You earned $', str(hours)*10)

#attempt 2 
hours = input('How many hours did you work? ')
answer =  hours * 10 
print ('You earned $', (answer))

# if alone 'hours * 10', this will be repeated over and over again as ity is a 
# string (text)
# you may be able to use string input as an int or float
# by default input is a string or text- need to convert to float or int

#attempt 3
hours=input('How many hours did you work? ')
answer=int(hours)*10 
print('You earned $', str(answer))

#attempt 4
hours=input('How many hours did you work? ')
answer=int(hours)*10 
print('You earned $', (answer))

#attempt 5
hours=int(input('How many hours did you work? '))
answer=(hours)*10 
print('You earned $', (answer))

#attempt 6
hours = int(input('How mnay hours did you work? '))
answer = hours * 10
statements = 'based on hours worked you earned $'
print('%s%d' %(statements, answer))

#attempt 7
hours=int(input('How mnay hours did you work? '))
answer=hours*10
print('based on hours worked, you earned $ %d' +  %(answer))

#Task 6- Loops and lists
#1. Assign the following colors to the list called items
# red, orange, yellow, green
#2. for the output display 1 red 2 orange 3 yellow 4 green
#Hint, for loop and print

items = ['red', 'orange', 'yellow','green']
x = 1
for i in items:
    print (x, i)
    x+=1 #increments, x = x + 1



