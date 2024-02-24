# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:32:51 2020

@author: Gabriel Melendez
"""

#%%

'''

HW_8_Pirple 

I/O

by Gabriel M
'''

import os.path
FileList = []

while(True):
    FileName = input('\nplease enter the file name: ')
    
    if os.path.isfile(FileName) == True: #A way to access an existing file in your computer
        FileList.append(FileName)
    
    if FileName == 'Chocolate': #*****This keyword will BREAK the loop******
        break              

    elif FileName in FileList:         #if the file does exist
        print('what do you wish to do with this file:',FileName,'?')
        options = input('A) Read the file\nB) Delete the file and start over\nC) Append the file\n\n')
        
        if options == 'A' or options == 'a':                #Option A = Read File
            openfile = open(f'{FileName}','r')
            for line in openfile:
                print(f'{line}', end='')
            openfile.close() 
                
        elif options == 'B' or options == 'b':                #Option B = Delete file and star over 
            with open(f'{FileName}','w') as file:
                usertext = input(f'what do you want to write in your new: {FileName}?\n\n') #user's text for the file
                file.write(usertext)
                file.close()
                
        elif options == 'C' or options == 'c':                 #Option C == append to the file
            with open(f'{FileName}','a') as file:
                usertext = input(f'what do you want to continue writing in {FileName}?\n\n') #user's text for the file
                file.write(f'\n{usertext}')
                file.close()
        
                
    else:                           #if the file does not exist 
        FileList.append(FileName)
        with open(f'{FileName}','w') as file:
            usertext = input('There is no record of this file, what do you want to write in your new file?\n\n') #user's text for the file
            file.write(usertext)
            file.close()

print('Recorded File List:', FileList)