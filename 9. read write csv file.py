# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:43:50 2022

@author: nza7
"""

#1 Import the csv file, write on csv, read csv output
# make a fields and columns for rows and columns
# csv means comma seperated files

import csv
fields = ['Name','Branch','Year','GPA'] # these are the data points/ column headers
rows = [['Larry', 'Engg', '2', '3.1'], ['Curley', 'IT', '1', '3.5'],
        ['Moe', 'Math', '2', '3.1'], ['Kelly', 'MIS', '1', '3.3'],
        ['Jill','Mgmt','3','2.8'], ['Sabrina', 'CS', '2', '3.8']]
# this is the list!it is a sequence
filename = 'university_records.csv'
#this is your file object, giving it a name with a .csv
# if the file exists, it will be overwritten if not, will be created
# write overwrites the file
with open (filename, 'w') as csvfile:
    # with and open statements-we want to opeb the file name which was declared abivem open with 'w' write position and as
    # a csv file
    csvwriter = csv.writer(csvfile)
    # we called the identifier csv.writter- this is the md
    csvwriter.writerow(fields) # this should be whatever is in fileds # multiple rows so we are using rows
    csvwriter.writerows(rows) # rowSSS with an s
    # we will now change the ecel files and remove the blank rows
with open (filename, newline = '') as f: # breaking it at a nwe line and open it as f not csv
    reader = csv.reader (f)
    for row in reader:
        print (row)  # used a for loop, for any identifier, for in the reader variable and then print the row
with open (filename) as input, open ('university_records1.csv', 'w') as output:
    no_blank = (line for line in input if line.strip())
    output.writelines(no_blank)
    # whatever existing in file, take as input
    # now we may read the new file
    