# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:44:34 2020

@author: Gabriel Melendez
"""


#%%

'''

Project_2_Pirple 

Hang Man

by Gabriel M
'''

#   _____  0
#   |   |  1
#   |   O  2
#   |  /|\ 3
#   |   |  4
#   |  / \ 5
#   |      6
# -------  7
# 012345678

import random
NumTimesWrong = 0

def PrintHangMan():
    for row in range(8):
        if row != 7:
            if row == 0:
                print('  _____  ')
            elif row == 1:
                print('  |   |  ')
            elif NumTimesWrong >= 1 and row == 2:
                print('  |   O  ')
                if NumTimesWrong >= 2:
                    if NumTimesWrong >= 5:
                        print('  |  /|\ ')
                        
                    elif NumTimesWrong >= 4:
                        print('  |   |\ ')
                        
                    else:
                        print('  |   |  ')
                if NumTimesWrong >= 3:
                    print('  |   |  ')
                if NumTimesWrong >= 6:
                    if NumTimesWrong >= 7:
                        print('  |  / \ ')
                    else:
                        print('  |  /  ')
            else:
                print('  |      ')   
        else:
            print('-'*6)


print('Welcome to Hang-Man')

Mode = input('1-player or 2-player mode: [1/2]  ')

if Mode == '2':
    SecretWord = input('Player 1 please choose a word: ')
    
    LengthInNum = len(SecretWord)
    SecretWordList = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    GuessedList= []
    WrongList = []
    CorrectList = []
    winner = 'Player 2'
    for Letter in range(LengthInNum):
        GuessedList.append('_ ')
    
    for letter in SecretWord:
        SecretWordList[letter]+=1
    
    for letter in SecretWord:
        CorrectList.append(letter)
    
    while (GuessedList != CorrectList):
        print('\n'*35)
        print(GuessedList)
        PrintHangMan()
        print(WrongList)
        if NumTimesWrong == 7:
            winner = 'Player 1'
            break
        LetterGuess = input('What letter do you guess?: ')
        if SecretWordList[LetterGuess] >= 1: #you got it right
            letterNum = 0
            for letter in SecretWord:
                if LetterGuess == letter:
                    GuessedList[letterNum] = LetterGuess
                letterNum +=1    
        else: #you got it wrong
            if LetterGuess in WrongList:
                continue
            WrongList.append(LetterGuess)
            NumTimesWrong += 1    
else:
    List1 = []
    badChars = '\n'
    openfile = open('HangManTest1','r')
    for line in openfile:
        for i in badChars:
            line = line.replace(i,'')
        List1.append(line)
    SecretWord = random.choice(List1)
    LengthInNum = len(SecretWord)
    SecretWordList = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    GuessedList= []
    WrongList = []
    CorrectList = []
    winner = 'Player 2'
    for Letter in range(LengthInNum):
        GuessedList.append('_ ')
    
    for letter in SecretWord:
        SecretWordList[letter]+=1
    
    for letter in SecretWord:
        CorrectList.append(letter)
        
    while (GuessedList != CorrectList):
        print('\n'*35)
        print(GuessedList)
        PrintHangMan()
        print(WrongList)
        if NumTimesWrong == 7:
            winner = 'Player 1'
            break
        LetterGuess = input('What letter do you guess?: ')
        if SecretWordList[LetterGuess] >= 1: #you got it right
            letterNum = 0
            for letter in SecretWord:
                if LetterGuess == letter:
                    GuessedList[letterNum] = LetterGuess
                letterNum +=1    
        else: #you got it wrong
            if LetterGuess in WrongList:
                continue
            WrongList.append(LetterGuess)
            NumTimesWrong += 1   
            
print('\n'*35)
print(GuessedList)
PrintHangMan()
print(WrongList)
print('\nThe Secret Word was:',SecretWord)
print('\nThe Winner is:', winner)
openfile.close() 
