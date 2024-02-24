# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:53:31 2020

@author: Gabriel Melendez
"""

#%%

'''

HW_5_Pirple 

FizzBuzz

by Gabriel M
'''


print('This is a program that allows the user print a list with the numbers you desire\nOnly positive numbers!')
starter = int(input('what number do you want the list to start with?:  '))
while starter < 0: ###loops the question until the starting value is positive
    starter = int(input('what number do you want the list to start with?:  '))
ender = int(input('what number do you want the list to end?:  '))
while ender < starter: ###loops the question if its a number less than the starting point
    ender = int(input('what number do you want the list to end?:  '))



#The Algorith works with every positive integer
for x in range(starter,ender+1):
    if x == 1 or x == 2 or x == 3 or x == 5 or x == 7: 
        print(f'Prime: {x}')
        continue    
    if ((ender+1)%x) == 0: #This checks if the number is prime
        print(f'Prime: {x}')
        continue
    if x%3 == 0 and x%5 == 0: #This checks if the number selected is both divisible by 3 & 5
        print(f'FizzBuzz: {x}') 
        continue
    if x%3 == 0: #This checks if the number selected is divisible by 3
        print(f'Fizz: {x}')
        continue
    if x%5 == 0: #This checks if the number selected is divisible by 5
        print(f'Buzz: {x}')
        continue
    print(x)

# =============================================================================
# %%
# =============================================================================

num = int(input('enter your number: '))
x = 2

if num > 1 :
    while x <= num:
        for y in range(x,num):
            print(x,y,num)
            if (num%y) == 0:
                print(y,'not prime')
            else:
                print(y,'is prime')
        x += 1
            
        
        