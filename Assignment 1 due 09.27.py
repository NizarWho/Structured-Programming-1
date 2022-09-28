# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:50:35 2022

@author: nza7
"""


#1-Someone said
quote='"When the world pushes you to your knees, you’re in the perfect position to pray-Rumi"'
print(quote)

#2-First Name Cases
name='nizar'
print(name)
print(name.title())
print(name.upper())

#3-Full name
firstname='Nizar '
lastname='Almoughrabi'
big_string=(firstname + lastname)
print(big_string)

#4-About this person
firstname='Milk'
lastname='Man'
big_string=(firstname + lastname)
print('The ' + big_string + ' is essential to the neighborhood')

#5-namespaces
firstname=' ' + 'Nizar' + ' '
print(firstname)
firstname2= 'Nizar'
print( firstname )
print(firstname.lstrip())
print(firstname.rstrip())
print(firstname.strip())

#6-Arithmetic
print(10+10,'Addition')
print(5-2,'Subtraction')
print(2*2,'Multipication')
print(3/2, 'Division')
print(3**2, 'Exponent')

#7-Order of operations
print(6 - 5 + 2)
print(6 - (5 + 2))

#8-Long decimals
print(12/8.12)

#9-Neat Arithmetic
addition=(10+10)
print(addition)
subtraction=(5-2)
print(subtraction)
multipication=(2*2)
print(multipication)
division=(3/2)
print(division)
exponent=(3**2)
print(exponent)
big_string=('The result of 10 + 10 = '  + str(addition) + '\n'
            'The result of 5 - 2 = ' + str(subtraction) + '\n'
            'The result of 2* * 2 = ' + str(multipication) + '\n'
            'The result of 3 / 2 = ' + str(division) + '\n'
            'The result of 3 ** 2 = ' + str(exponent) + '\n')
print(big_string)

#10-Neat order of operations
op1=(6 - 5 + 2)
op2=(6 - (5 + 2))
big_string=(op1, op2)
print(big_string)
print('For the above reslt (3) is (6 - 5 + 2) and (6 - (5 + 2) is -1. Reason why they are diffrent is due to the rules of PEMDAS')

#11-Long decimals-pattern
big_string=('the pattern is based on floating point arithmetic' + '\n' +
      'To expand: any number with a denominator fraction of 2 digits will result in leading decimals' + '\n' +
      'For example:' + '1/1- gives you:' + str(1/10) +'1/5 gives you:' + str(1/5) +'\n' +
      'the simplest way to understand it as it looks x/2 digit gives you repeating and x/2! digits does not')
print(big_string)




