# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:44:03 2022

@author: nizar
"""

# TASK 1
#1. Import the csv package
#2. Read the winequality-red.csv file
#3. With open create the csv.reader object
#4. Pass the keyword arguement delimiter=';' this is to make sure that the date split at the ;
#5. call list type to get all the rows
#6. Assign the results to an identifier called wines
#7. Print wines

import csv

with open('winequality-red.csv', 'r') as red:
   wines = list(csv.reader(red, delimiter = ';'))
   print(wines)
   
# Print the first three rows

import csv

with open('winequality-red.csv', 'r') as red:
   wines = list(csv.reader(red, delimiter = ';'))
   print(wines[0:3])
   
# Task 2- Extract the last element from each row after the header row
#1. Convert each extracted element to a float
#2. Assign all the extracted values to a list called qualities
#3. Divide the sum of the quality by the total number of elements/values in quality to get the mean
#4. Print the values

import csv

with open('winequality-red.csv', 'r') as red:
   wines = list(csv.reader(red, delimiter = ';'))
   qualities = [float(item[-1]) for item in wines[1:]]
   a = sum(qualities) / len(qualities)
   print(a)

# Task 3- Print the first 5 rows formatted

import csv
filename = 'winequality-red.csv'

# Initiate the titles (col headers) & the data (rows)

fields = []
rows = []

# read the csv file

with open(filename, 'r') as csvfile:
    # create the csv.reader object
    csvreader=csv.reader(csvfile)
    
    # Extract the field name/Col header for the 1st row
    fields = next(csvreader)
    
    # Extract the data for each row (1 by 1)
    for row in csvreader:
        rows.append(row)
        
    # get the total number of rows
    print('Total # of rows: %d' %(csvreader.line_num))
    
    # print fields name/column header
    print('column name are: ' + ';' .join(field for field in fields))
    
# print the first 5 rows of data!

print ('\n First 5 rows: \n')
for row in rows[:5]:
    #print each column (parsing) 
    for col in row:
        print(col)
    
    
    
    