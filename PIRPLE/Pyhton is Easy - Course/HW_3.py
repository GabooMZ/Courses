# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:15:56 2020

@author: Gabriel Melendez
"""


#%%
'''

Hw_3_Pirple

If Statements 

Gabriel Meléndez
'''

print('This progam determines if any of the 3 given variables are the same as the others')

a=0

def param(a,b,c): #Works with letters and numbers
    if a == b or a == c or b == c:
        return True
    else:
        return False

x = input('what is the value of x?:  ') 
y = input('what is the value of y?:  ')  
z = input('what is the value of z?:  ')    
 
print(param(x,y,z))
print(a)

