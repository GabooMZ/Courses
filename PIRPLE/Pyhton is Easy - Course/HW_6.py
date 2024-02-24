# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:54:10 2020

@author: Gabriel Melendez
"""


#%%

'''

HW_6_Pirple 

Advanced Loops

by Gabriel M
'''
 
# 35 characters Height & 81 characters width

 
def playboard(x,y): #x = number of rows/height & y = number of columns/width
    for row in range(x):
        if row%2 == 0:
            for column in range(1,y+1):
                if column%2 == 1:
                    if column != y:
                        print(' ',end='')
                    else:
                        print(' ')
                else:
                    print('|', end='')
        else:
            print('-'*y)
    if x >= 1 and x <= 35: # This returns the value of the function True or False depending if excedes the parameters
        if y >= 1 and y <= 81:
            return True
        else:
            return False
    else:
        return False
        
# playboard(5,5)


x = int(input('how many rows/height do you want?:  '))
y = int(input('how many columns/width do you want?:  '))

print(playboard(x,y))