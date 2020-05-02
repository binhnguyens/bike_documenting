#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:11:14 2020

@author: binhnguyen
"""


import csv
import tkinter as tk
from tkinter import simpledialog
import time
from tkinter.filedialog import askopenfilename


# Ask which file to write to 
file = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print('Your file is: ',file)
time.sleep (1)

# Data input
def input(prompt1):
    ROOT = tk.Tk()
    ROOT.withdraw()
    # the input dialog
    USER_INP = simpledialog.askstring(title="New Entry", prompt=prompt1)
    return USER_INP

date = input('Date: ')
part = input('Part: ')
money = input('Money: ')
description = input('Description: ')
cum = [date,money,part,description] # change this for extra stuff

# Reading file
rows =[]
with open(file) as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        rows.append(row)
        

# Data write 
with open(file, 'w') as csvfile:
    fieldnames = ['Date', 'Money', 'Part', 'Description'] # change this for extra stuff
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for i in range (1,len(rows)):
        writer.writerow({rows[0][0]: rows[i][0], rows[0][1]: rows[i][1], rows[0][2]: rows[i][2], 
                         rows[0][3]:rows[i][3]}) # change this for extra stuff
        
    writer.writerow({rows[0][0]: cum[0], rows[0][1]: cum[1], rows[0][2]: cum[2], 
                         rows[0][3]:cum[3]}) # change this for extra stuff
 
    
# Final messages
time.sleep (1)
print("Writing complete")
time.sleep (1)
print ("...........")
time.sleep (2)
print ('Updated file:')
with open(file) as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print (row)

