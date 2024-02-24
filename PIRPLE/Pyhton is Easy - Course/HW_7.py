# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 13:11:14 2020

@author: Gabriel Melendez
"""


#%%

'''

HW_7_Pirple 

Dictionaries & Sets

by Gabriel M
'''

# Artist = 'Queen'
# Genre = 'Classic Rock or Rock'
# Duration= 354
# Composer = 'Freddie Mercury'
# Form = 'Song'
# Theme = 'Loneliness'
# Texture = 'Homophony'

songdescription = {'Artist': 'Queen', 'Genre': 'Classic Rock' or 'Rock','Duration': '354seconds', 'Composer': 'Freddie Mercury', 'Form': 'Song', 'Theme': 'Loneliness', 'Texture': 'Homophony' }
for description in songdescription:
    print(f'{description} = {songdescription[description]}')
    
def guess():
    key = input('What do you want to guess from the song Bohemian Rhapsody?  ')
    if key in songdescription:
        answer = input('What is your guess? ')
        if answer in songdescription[key]:
            print('\nYou are correct!')
            return True
        else:
            print('\nYou are wrong')
            return False
    else:
        print('Sorry that description is not available')

print(guess())
    