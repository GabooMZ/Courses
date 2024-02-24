# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:12:03 2020

@author: Gabriel Melendez
"""


#%%

'''

HW_11_Pirple 

Error Handling

by Gabriel M
'''

## YOU MAY DO AS MANY TESTS AS YOU WANT ##
## IT WILL ONLY PRINT THE BOARD IF A INTEGER IS ENTERED ##
## AND IF IT IS A POSITIVE INTEGER WITH THE PARAMETERS BELOW ##
## PARAMETERS FOR THE BOARD ARE FOR MY PERSONAL COMPUTER, APOLOGIES ##

# 35 characters Height & 80 characters width

 
def playboard(x,y): #x = number of rows/height & y = number of columns/width
    if x >= 1 and x <= 35: # This returns the value of the function True or False depending if excedes the parameters
        pass
    else:
        return ('Can not create a board with this parameter: x =', x)
    if y >= 1 and y <= 80:
        pass
    else:
        return ('Can not create a board with this parameter: y =', y)
    
    for row in range(x):
        print('')
        if row%2 == 0:
            for column in range(0,y):
                if column%2 == 0:
                        print(' ',end='')
                else:
                    print('|', end='')
        else:
            print('-'*y,end='')
    print('')
    return True

x = ''
y = ''
while isinstance(x, int) != True:
    x = input('how many rows/height do you want?:  ') 
    try:
        x = int(x)
    except:
        continue
    
while isinstance(y, int) != True:
    y = input('how many columns/width do you want?: ') 
    try:
        y = int(y)
    except:
        continue

print(playboard(x,y))