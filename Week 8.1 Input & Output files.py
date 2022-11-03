# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:45:21 2022

@author: nza7
"""

# 11/03/2022- I/O inout and output
# Easiest way is using print statment- 

# Example: 

fo = open ('foo.txt', 'wb')
fo.writer = ('Python is a great language. \nYeah it is great! \n');
# close file
fo.close()

# Open a file
fo = open ('foo.txt', 'r+')
str = fo.read(20);
print ('Read String is :', str)
# Close file

# Check current position
position = fo.tell();
print ('Current file position :', position)

position = fo.seek (0, 1);
str = fo.read (10);
print ('Again read string is', str)
#close aoend file
fo.close()

