# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:57:58 2020

@author: Gabriel Melendez
"""


#%%

'''
HW_4_Pirple 

Lists

by Gabriel M
'''

myuniquelist = []
myleftovers = []

#algorithm
def addto(x):
    if len(myuniquelist) >= 1: #ensuring the first value of the list is not counted the first time
        if x in myuniquelist: #if the value is in the list it goes to leftover
            myleftovers.append(x)
        else:#otherwise it's added to the list
            myuniquelist.append(x)
    else: 
        myuniquelist.append(x)

#Tests
addto(1)
print('list: ', myuniquelist)
print('leftover: ', myleftovers)
addto(2)
print('list: ', myuniquelist)
print('leftover: ', myleftovers)
addto(2)
print('list: ', myuniquelist)
print('leftover: ', myleftovers)
addto(5)
print('list: ', myuniquelist)
print('leftover: ', myleftovers)
addto(1)
print('list: ', myuniquelist)
print('leftover: ', myleftovers)