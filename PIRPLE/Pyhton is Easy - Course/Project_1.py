# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:47:16 2020

@author: Gabriel Melendez
"""


#%%

'''

Project_1_Pirple 

Connect 4

by Gabriel M
'''


#  1 2 3 4 5 6 7 8
# 012345678901234567
# |1|2|3|4|5|6|7|8|
# | | | | | | | | |+1%1 = 0
# | | | | | | | | |+3%2 = 1 
# | | | | | | | | |+5%3 = 2
# | | | | | | | | |+7%4 = 3
# | | | | | | | | |+8%5 = 4
# | | | | | | | | |+11%6 = 5
# 

PlayerTurn = 1
ListofMoves = []
winner = 'no one'
Boardcolumns = [1,2,3,4,5,6,7,8]
def board(): # prints the first empty board
    print('\n'*28)
    print('|1|2|3|4|5|6|7|8|')
    for row in range(1,7):
        RowList =[]
        ListofMoves.append(RowList)
        for column in range(18):
            if column%2 == 1:
                if column != 17:
                    print('.',end='')
                    PotentialSpace = '.'
                    RowList.append(PotentialSpace)
                else:
                    print(' ')
            else:
               print('|', end='')
board()
def Userboard(): #this is the board that can be modified
    print('|1|2|3|4|5|6|7|8|')
    for row in ListofMoves:
        for column in row:
            print('|', end='')
            print(column, end='')
        print('|')
        
while(winner == 'no one'): #player turns
    
    while PlayerTurn == 1 and winner == 'no one': #player 1 turn
        x = 0
        z = -1
        PlayerMove = int(input(f'Which column would you like to place your token at Player: {PlayerTurn}?  '))
        while PlayerMove != 1 and PlayerMove != 2 and PlayerMove != 3 and PlayerMove != 4 and PlayerMove != 5 and PlayerMove != 6 and PlayerMove != 7 and PlayerMove != 8: 
            PlayerMove = int(input(f'Which column would you like to place your token at Player: {PlayerTurn}?  '))
        while ListofMoves[-1+x][PlayerMove-1] == 'O' or ListofMoves[-1+x][PlayerMove-1] == 'X':
            x-= 1
            z -=1
        ListofMoves[z][PlayerMove-1] = 'O'  #####
        print('\n'*28)
        Userboard()       
        WinnerList = []    
        for row in ListofMoves: #####algorithm for winning Horizontally#####
            k = 0
            while k != 8:
                WinnerList.append(row[k])
                k += 1
                if len(WinnerList) == 4:        
                    k -= 3
                    if WinnerList == ['O','O','O','O']: #####
                       winner = 'player 1 won!' ######
                    else:
                        WinnerList = []
            if k == 8:
                WinnerList = []
        row = 0            
        for repeat in range(6):  #####Algorithm for winning diagonally to the right######            
            if repeat== 5:
                break
            WinnerList = []
            row = 0
            column = repeat
            for columns4 in range(4):                
                if columns4 == 3:
                    break
                WinnerList = []
                while len(WinnerList) != 4:
                    elements = ListofMoves[row][column]
                    row += 1
                    column += 1
                    WinnerList.append(elements)                    
                if WinnerList == ['O','O','O','O']: #####
                    winner = 'player 1 won!' ######                
                WinnerList = []
                row -= 3
                column -= 4
        PlayerTurn = 2    
        for repeat in range(-1,-6,-1):  #####Algorithm for winning diagonally to the left######
            if repeat== 5:
                break
            WinnerList = []
            row = 0
            column = repeat
            for columns4 in range(4):            
                if columns4 == 3:
                    break
                WinnerList = []
                while len(WinnerList) != 4:
                    elements = ListofMoves[row][column]
                    row += 1
                    column -= 1
                    WinnerList.append(elements)                    
                if WinnerList == ['O','O','O','O']: #####
                    winner = 'player 1 won!' ######               
                WinnerList = []
                row -= 3
                column += 4
        for repeat in range(8):  #####Algorithm for winning vertically######
            WinnerList = []
            row = 0
            for columns4 in range(4):
                if columns4 == 3:
                    break
                WinnerList = []
                while len(WinnerList) != 4:
                    elements = ListofMoves[row][repeat]
                    row += 1
                    WinnerList.append(elements)
                if WinnerList == ['O','O','O','O']: #####
                    winner = 'player 1 won!' ######
                WinnerList = []
                row -= 3
    while PlayerTurn == 2 and winner == 'no one': #player 2 turn
        x = 0
        z = -1        
        PlayerMove = int(input(f'Which column would you like to place your token at Player: {PlayerTurn}?  '))
        while PlayerMove != 1 and PlayerMove != 2 and PlayerMove != 3 and PlayerMove != 4 and PlayerMove != 5 and PlayerMove != 6 and PlayerMove != 7 and PlayerMove != 8: 
            PlayerMove = int(input(f'Which column would you like to place your token at Player: {PlayerTurn}?  '))
        while ListofMoves[-1+x][PlayerMove-1] == 'O' or ListofMoves[-1+x][PlayerMove-1] == 'X':
            x-= 1
            z -=1
        ListofMoves[z][PlayerMove-1] = 'X'  #####
        print('\n'*28)
        Userboard()
        WinnerList = []             
        for row in ListofMoves: ######Algorith for winning Horiziontally #####
            k = 0
            while k != 8:
                WinnerList.append(row[k])
                k += 1
                if len(WinnerList) == 4:        
                    k -= 3
                    if WinnerList == ['X','X','X','X']: ######
                       winner = 'player 2 won!' #######
                    else:
                        WinnerList = []
            if k == 8:
                WinnerList = []
        row = 0
        for repeat in range(6):  #####Algorithm for winning diagonally to the right######
            if repeat== 5:
                break
            WinnerList = []
            row = 0
            column = repeat
            for columns4 in range(4):
                if columns4 == 3:
                    break
                WinnerList = []
                while len(WinnerList) != 4:
                    elements = ListofMoves[row][column]
                    row += 1
                    column += 1
                    WinnerList.append(elements)
                if WinnerList == ['X','X','X','X']: #####
                    winner = 'player 2 won!' ######
                WinnerList = []
                row -= 3
                column -= 4
        PlayerTurn = 1
        
        for repeat in range(-1,-6,-1):  #####Algorithm for winning diagonally to the left######
            if repeat== 5:
                break
            WinnerList = []
            row = 0
            column = repeat
            for columns4 in range(4):
                
                if columns4 == 3:
                    break
                WinnerList = []
                while len(WinnerList) != 4:
                    elements = ListofMoves[row][column]
                    row += 1
                    column -= 1
                    WinnerList.append(elements)
                    
                if WinnerList == ['X','X','X','X']: #####
                    winner = 'player 2 won!' ######
                
                WinnerList = []
                row -= 3
                column += 4        
        for repeat in range(8):  #####Algorithm for winning vertically######
            WinnerList = []
            row = 0
            for columns4 in range(4):
                if columns4 == 3:
                    break
                WinnerList = []
                while len(WinnerList) != 4:
                    elements = ListofMoves[row][repeat]
                    row += 1
                    WinnerList.append(elements)
                    
                if WinnerList == ['X','X','X','X']: #####
                    winner = 'player 2 won!' ######
                WinnerList = []
                row -= 3    
print('')        
print(winner)                      