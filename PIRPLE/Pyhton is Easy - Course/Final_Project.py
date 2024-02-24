'''

Project_3_Pirple 

Pick A Card Game! -> Texas Hold 'Em Poker

by Gabriel M
'''

# ┌─────┐  0
# | 10  |  1
# |  ♣  |  2
# |  10 |  3
# └─────┘  4
# 012345678    

# ┌─────┐  0
# | 1   |  1
# |  ♣  |  2
# |   1 |  3
# └─────┘  4
# 0123456   


from random import shuffle
from time import sleep
from itertools import combinations
from termcolor import colored
# import Functions as FF
CardDeck = []


def CreateDeck():  ##USED TO CREATE AND SHUFFLE A DECK OF CARDS
    FourSuits = ['♠','♥','♦','♣']
    SpecialCards = ['A','J','Q','K']
    for suits in FourSuits:
        for pips in range(2,11):
            Card = str(pips)+suits
            CardDeck.append(Card)
        for cards in SpecialCards:
            Card = cards+suits
            CardDeck.append(Card)
    shuffle(CardDeck)
    
def PrintCards(Hand = []):
    Char1 = '♠'
    Char2 = '♣'
    for row in range(5):
        if row != 0:
            print('')
        if row == 0:
            for x in range(len(Hand)):
                print('┌─────┐ ',end = '')
        if row == 4:
            for x in range(len(Hand)):
                print('└─────┘ ',end = '')
        else:
            for card in Hand:
                if Char1 in card or Char2 in card:
                    color = 'grey'
                else:
                    color = 'red'
                CardVal = []
                if len(card) != 3: #Print the cards that are not 10
                    Type = 1
                else:
                    Type = 2
                CardVal = []
                for Val in card:  
                    CardVal.append(Val)
                if row == 1:
                    if Type == 1:
                        print('| '+colored(CardVal[0],str(color),attrs=['bold'])+'   | ',end = '')
                    if Type == 2:
                        print('| '+colored(CardVal[0]+CardVal[1],str(color),attrs=['bold'])+'  | ',end = '')
                if row == 2:
                    if Type == 1:
                        print('|  '+colored(CardVal[1],str(color),attrs=['bold'])+'  | ' ,end = '')
                    if Type == 2:
                        print('|  '+colored(CardVal[-1],str(color),attrs=['bold'])+'  | ',end = '')
                if row == 3:
                    if Type == 1:
                        print('|   '+colored(CardVal[0],str(color),attrs=['bold'])+' | ' ,end = '')
                    if Type == 2:
                        print('|  '+colored(CardVal[0]+CardVal[1],str(color),attrs=['bold'])+' | ',end = '')

# =============================================================================
# =============================================================================
# # 
# =============================================================================
# =============================================================================
# RF_Cards= ['10♥','J♥','Q♥','K♥','A♥']

def Royal_Flush(Five_Cards):       ######CHECK
    FourSuits = ['♠','♥','♦','♣']
    Five_Types = ['10','J','Q','K','A']
    for Suit in FourSuits:
        RF_li = []
        for Type in Five_Types:
            The_Card = Type + Suit
            RF_li.append(The_Card)
        if set(RF_li) == set(Five_Cards):
            return [10,Five_Cards,'Royal Flush']
    return [0]


# print(Royal_Flush(RF_Cards))
# =============================================================================
# 
# =============================================================================
def SF_on_RF_Check(Five_Cards):    ######CHECK
    FourSuits = ['♠','♥','♦','♣']
    for Suit in FourSuits:
        A_Card = 'A' + Suit
        if A_Card in Five_Cards:
            return False #Do not execute Straight_Flush
        else:
            return True  #Execute Straight_Flush
        
        
# SF_Cards = ['9♣','10♣','K♣','Q♣','J♣'] 
       
def Straight_Flush(Five_Cards):    ######CHECK
    x = SF_on_RF_Check(Five_Cards)    #This makes sure that your Straight Flush Can not be a Royal one
    if x == False:
        return [0]
    else:
        FourSuits = ['♠','♥','♦','♣']
        Cards = {2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K'}
        
        for Suit in FourSuits:     #Algorithm that determines if you have a Straight Flush
            Value_of_Set = 0.02
            for Num in range(2,10):
                SF_li = []
                for plus_num in range(5):
                    The_Card = Cards[Num+plus_num]+Suit
                    SF_li.append(The_Card)
                if set(SF_li) == set(Five_Cards):
                    return [9 + Value_of_Set,Five_Cards,'Straigh Flush']
                else:
                    Value_of_Set += 0.01
    return [0]
    
# print(Straight_Flush(SF_Cards))   
# =============================================================================
#    
# =============================================================================
# FOAK_Cards = ['6♠','4♥','6♦','6♣','6♣']

def FOAK(Five_Cards):       ######CHECK
    All_Cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    FourSuits = ['♠','♥','♦','♣']
    Value_of_Set = 0.02
    Updt_Five_Cards = []
    for card in Five_Cards:
        Updt_Five_Cards.append(card)
        
    for element in range(len(Updt_Five_Cards)):    #This takes care of special Chars
        for suit in FourSuits:
            Updt_Five_Cards[element] = Updt_Five_Cards[element].replace(suit,'')
            
    for Card_Type in All_Cards:   #Algorithm that determines if you have 4 of a Kind
        FOAK_Checker = 0
        for card in Updt_Five_Cards:
            if card == Card_Type:
                FOAK_Checker += 1
            if FOAK_Checker == 4:
                return [8 + Value_of_Set,Five_Cards,'Four of a Kind']
            
        Value_of_Set += 0.01
    return [0]

# print(FOAK(FOAK_Cards))   
# =============================================================================
#     
# =============================================================================
# FH_Cards = ['A♠','J♥','J♦','A♣','A♣']

def Full_House(Five_Cards):          ######CHECK
    FourSuits = ['♠','♥','♦','♣']
    All_Cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    Value_of_Set = 0.02
    Updt_Five_Cards = []
    for card in Five_Cards:
        Updt_Five_Cards.append(card)
        
    for element in range(len(Updt_Five_Cards)):    #This takes care of special Chars
        for suit in FourSuits:
            Updt_Five_Cards[element] = Updt_Five_Cards[element].replace(suit,'') 
            
    for First_3 in All_Cards:   #Algorithm that determines if you have a Full House
        Full_House_li = []
        for z in range(3):
            Full_House_li.append(First_3)
        for Last_2 in All_Cards:
            if Last_2 == First_3:
                continue
            for z in range(2):
                Full_House_li.append(Last_2)
            if sorted(Full_House_li) == sorted(Updt_Five_Cards):
                return [7 + Value_of_Set,Five_Cards,'Full House']
            
            for z in range(2):
                Full_House_li.pop()
            
        Value_of_Set += 0.01
            
    return [0]  
  
# print(Full_House(FH_Cards))
# =============================================================================
# 
# =============================================================================
# Flush_Cards = ['A♠','J♥','J♦','A♣','A♣']   

def Flush(Five_Cards):                ######CHECK

    FourSuits = ['♠','♥','♦','♣']
    Updt_Five_Cards = []
    for card in Five_Cards:
        Updt_Five_Cards.append(card)
    for element in range(len(Updt_Five_Cards)):
        for suit in FourSuits:
            Updt_Five_Cards[element] = Updt_Five_Cards[element].replace(suit,'')   
            
    Crrnt_Value_of_Set = 0.02
    Card_Values = {'2':0.02,'3':0.03,'4':0.04,'5':0.05,'6':0.06,'7':0.07,'8':0.08,'9':0.09,'10':0.1,'J':0.11,'Q':0.12,'K':0.13,'A':0.14}
    
    for x in Card_Values:              #This gives a value to your Five Cards
        Value = Card_Values[x]
        if x in Updt_Five_Cards:
            if Value > Crrnt_Value_of_Set:
                Crrnt_Value_of_Set = Value
            
    for suit in FourSuits:             #This makes sure you have the cards required for a Flush
        Flush_Checker= 0
        for card in Five_Cards:
            if suit in card:
                Flush_Checker += 1
            else:
                pass
            if Flush_Checker == 5:
                return [6+Crrnt_Value_of_Set,Five_Cards,'Flush']
    return [0]
                
# print(Flush(Flush_Cards))      
# =============================================================================
#     
# =============================================================================
# Straight_Cards = ['A♣','10♥','K♣','Q♠','J♣']

def Straight(Five_Cards):                 ######CHECK
    FourSuits = ['♠','♥','♦','♣']
    Cards = {2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K',14:'A'}
    Updt_Five_Cards = []
    Value_of_Set = 0.02
    for card in Five_Cards:
        Updt_Five_Cards.append(card)
    for element in range(len(Updt_Five_Cards)):
        for suit in FourSuits:
            Updt_Five_Cards[element] = Updt_Five_Cards[element].replace(suit,'')   

    for Num in range(2,11): #Algorithm that determines if you have a Straight
        Straight_li = []
        for plus_num in range(5):
            The_Card = Cards[Num+plus_num]
            Straight_li.append(The_Card)
        if set(Straight_li) == set(Updt_Five_Cards):
            return [5 + Value_of_Set,Five_Cards,'Straight']
        else:
            Value_of_Set += 0.01
    return [0]

# print(Straight(Straight_Cards))
# =============================================================================
# 
# =============================================================================
# TOAK_Cards = ['J♠','7♥','J♦','2♣','J♣']

def TOAK(Five_Cards):                    ######CHECK  
    All_Cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    Value_of_Set = 0.02
    FourSuits = ['♠','♥','♦','♣']
    Updt_Five_Cards = []
    for card in Five_Cards:
        Updt_Five_Cards.append(card)
        
    for element in range(len(Updt_Five_Cards)):    #This takes care of special Chars
        for suit in FourSuits:
            Updt_Five_Cards[element] = Updt_Five_Cards[element].replace(suit,'')
            
    for Card_Type in All_Cards:   #Algorithm that determines if you have 3 of a Kind
        TOAK_Checker = 0
        for card in Updt_Five_Cards:
            if card == Card_Type:
                TOAK_Checker += 1
            if TOAK_Checker == 3:
                return [4 + Value_of_Set,Five_Cards,'Three of a Kind']
            
            Value_of_Set += 0.01
    return [0]

# print(TOAK(TOAK_Cards))
# =============================================================================
#     
# =============================================================================

# Two_Pairs_Cards = ['A♠','7♥','K♦','K♣','7♣']

def Two_Pairs(Five_Cards):          ######CHECK  
    Value_of_Set1 = 0
    Updt_Five_Cards = []
    FourSuits = ['♠','♥','♦','♣']
    Two_Pairs_Checker = 0
    Card_Values = {'2':0.02,'3':0.03,'4':0.04,'5':0.05,'6':0.06,'7':0.07,'8':0.08,'9':0.09,'10':0.1,'J':0.11,'Q':0.12,'K':0.13,'A':0.14}
    Card_Check = []
    for card in Five_Cards:
        Updt_Five_Cards.append(card)
    
    for element in range(len(Updt_Five_Cards)):    #This takes care of special Chars
        for suit in FourSuits:
            Updt_Five_Cards[element] = Updt_Five_Cards[element].replace(suit,'')
    Updt_Five_Cards.sort() 
    
    for cardnum in range(len(Updt_Five_Cards)-1):
        if Updt_Five_Cards[cardnum] == Updt_Five_Cards[cardnum+1]:
            if Updt_Five_Cards[cardnum] in Card_Check:
                 continue
            else:
                Card_Check.append(Updt_Five_Cards[cardnum])
                Two_Pairs_Checker += 1
           
        if Two_Pairs_Checker == 2:
            for card in Card_Check:
                Valueof_Card = Card_Values[card]
                if Valueof_Card > Value_of_Set1:
                    if Value_of_Set1 != 0:
                        Value_of_Set2 = Value_of_Set1/100
                        Value_of_Set1 = Valueof_Card
                    else: 
                        Value_of_Set1 = Valueof_Card    
                else:
                    Value_of_Set2 = Valueof_Card/100
            return [3 + Value_of_Set1+Value_of_Set2,Five_Cards,'Two Pairs']
    return [0]

# print(Two_Pairs(Two_Pairs_Cards))
# =============================================================================
# 
# =============================================================================
# One_Pairs_Cards = ['A♠','7♥','2♦','K♣','7♣']

def One_Pairs(Five_Cards):          ######CHECK  
    Value_of_Set = 0.02
    Updt_Five_Cards = []
    FourSuits = ['♠','♥','♦','♣']
    One_Pairs_Checker = 0
    Card_Values = {'2':0.02,'3':0.03,'4':0.04,'5':0.05,'6':0.06,'7':0.07,'8':0.08,'9':0.09,'10':0.1,'J':0.11,'Q':0.12,'K':0.13,'A':0.14}
    Card_Check = []
    for card in Five_Cards:
        Updt_Five_Cards.append(card)
    
    for element in range(len(Updt_Five_Cards)):    #This takes care of special Chars
        for suit in FourSuits:
            Updt_Five_Cards[element] = Updt_Five_Cards[element].replace(suit,'')
    Updt_Five_Cards.sort() 
    
    for cardnum in range(len(Updt_Five_Cards)-1):
        if Updt_Five_Cards[cardnum] == Updt_Five_Cards[cardnum+1]:
            if Updt_Five_Cards[cardnum] in Card_Check:
                continue
            else:
               Card_Check.append(Updt_Five_Cards[cardnum])
               One_Pairs_Checker += 1
           
        if One_Pairs_Checker == 1:
            for card in Card_Check:
                Valueof_Card = Card_Values[card]
                if Valueof_Card > Value_of_Set:
                    Value_of_Set = Valueof_Card
            return [2 + Value_of_Set,Five_Cards,'One Pair']
    return [0]

# print(One_Pairs(One_Pairs_Cards))
# =============================================================================
# 
# =============================================================================
# High_Card_Cards = ['6♠','7♥','2♦','4♣','3♣']

def High_Card(Five_Cards):          ######CHECK  
    Value_of_Set = 0.02
    Updt_Five_Cards = []
    FourSuits = ['♠','♥','♦','♣']
    Card_Values = {'2':0.02,'3':0.03,'4':0.04,'5':0.05,'6':0.06,'7':0.07,'8':0.08,'9':0.09,'10':0.1,'J':0.11,'Q':0.12,'K':0.13,'A':0.14}
    for card in Five_Cards:
        Updt_Five_Cards.append(card)
    
    for element in range(len(Updt_Five_Cards)):    #This takes care of special Chars
        for suit in FourSuits:
            Updt_Five_Cards[element] = Updt_Five_Cards[element].replace(suit,'')
    Updt_Five_Cards.sort() 
    
    for card in Updt_Five_Cards:
        Valueof_Card = Card_Values[card]
        if Valueof_Card > Value_of_Set:
            Value_of_Set = Valueof_Card
    return [1 + Value_of_Set,Five_Cards,'High Card']

# print(High_Card(High_Card_Cards))
# =============================================================================
# =============================================================================
    
class Player: ###Call, Raise, Fold, Bet, Check
    def __init__(self, chips):
        self.total_chips = chips
        self.CurrentBet = 0
        
        
    def Check(self):
        pass
    
    def Bet(self,Val_bet):
        self.CurrentBet = Val_bet
            
    def Call(self, Match_bet):
        self.CurrentBet = Match_bet
        
    def Raise(self, RaiseBetNum):
        self.CurrentBet = RaiseBetNum
        
    def Fold(self):
        self.CurrentBet = 0
        
    def SmallBlind(self,bet):
        self.CurrentBet = bet
        
    def BigBlind(self,bet):
        self.CurrentBet = bet
        
    def endofRound(self):
        self.total_chips -= self.CurrentBet
        self.CurrentBet = 0
        
    def Win(self,The_Pot):
        self.total_chips += The_Pot
    
    def Winners(self,The_Pot,Winners):
        The_Pot = round(The_Pot/Winners)
        self.total_chips += The_Pot
        
    def __str__(self):
        return ('You have '+str(int(self.total_chips)-int(self.CurrentBet))+' '+colored('chips', 'red', attrs=['bold']))


def set_SB_Bet(SB): #FUNCTION THAT SETS THE SMALL BLIND BET
    z = False
    while isinstance(SB, int) != True or z != True:  ## The Small Blind Bet
                SB = input('\n'+colored(TheSmallBlind, 'yellow', attrs=['bold'])+', you are the Small Blind, what is your bet?: ')
                try:
                    SB = int(SB)
                    if SB > 0:
                        z = True
                    else:
                        continue
                except:
                    continue
    return SB

def set_BB_Bet(BB, SB): # FUNCTION THAT SETS THE BIG BLIND BET
    
    z = False
    while isinstance(BB, int) != True or z != True:  ## The Small Blind Bet
            BB = input('\n'+colored(TheBigBlind, 'yellow', attrs=['bold'])+', you are the Big Blind, what is your bet?: ')
            try:
                BB = int(BB)
                if BB > SB:
                    z = True
                else:
                    continue
            except:
                continue
    return BB


def Turn_Options(Nameof_Player, Currnt_Highest_Bet):
    while True:
        if Currnt_Highest_Bet > 0:  #Fold, Call, Raise
            Users_Path = input('\nA) Fold) To Fold is to discard ones hand and forfeit interest in the current pot.'+
                               '\n\nB) Call) To call is to match a bet or match a raise'+
                               '\n\nC) Raise) To Raise is to increase the size of the existing bet in the current betting round.'+
                               '\n\nD) See your hand) This options allows you, '+colored(Nameof_Player, 'yellow', attrs=['bold'])+', to see your cards.\n\n'+colored('Answer: ', 'green', attrs=['bold']))
        else:  #Fold, Bet, Check
             Users_Path = input('\nA) Fold) To Fold is to discard ones hand and forfeit interest in the current pot.'+
                           '\n\nB) Bet) You can Bet – If youre the first person in the round to make a bet, youre betting.'+
                           '\n\nC) Check) To Check means that the action passes to the player on your left without us making any wager.'+
                           '\n\nD) See your hand) This options allows you, '+colored(Nameof_Player, 'yellow', attrs=['bold'])+', to see your cards.\n\n'+colored('Answer: ', 'green', attrs=['bold']))
        while True:
            while Users_Path != 'A' and  Users_Path != 'a' and  Users_Path != 'B' and Users_Path != 'b' and  Users_Path != 'C' and  Users_Path != 'c' and  Users_Path != 'D' and  Users_Path != 'd':
                    Users_Path = input(colored('Answer: ', 'green', attrs=['bold']))
                    
            if Currnt_Highest_Bet > 0:  #Fold, Call, Raise

                if Users_Path == 'A' or Users_Path == 'a': ##### fold
                    if Nameof_Player in PlayerNames:
                        globals()[Nameof_Player].Fold()
                        RoundNames.remove(Nameof_Player)
                        PlayerCards_dict.pop(Nameof_Player)
                        return [f'{Nameof_Player} Folded','F']
                    
                elif Users_Path == 'B' or Users_Path == 'b':##### call
                    globals()[Nameof_Player].Call(Currnt_Highest_Bet)
                    if globals()[Nameof_Player].total_chips < 0:
                        PlayerNames.remove(Nameof_Player)
                        return [f'{Nameof_Player} Folded due to lack of chips']
                    else:
                        return [f'{Nameof_Player} Called']
                
                elif Users_Path == 'C' or Users_Path == 'c':                   ##### raise
                    z = False
                    Val_Raise_Bet = 0
                    while isinstance(Val_Raise_Bet, int) != True or z != True:
                        Val_Raise_Bet = input('What is the amount you want to raise the bet to?: ')
                        try:
                            Val_Raise_Bet = int(Val_Raise_Bet)
                            if Val_Raise_Bet > Currnt_Highest_Bet:
                                z = True
                            else:
                                continue
                        except:
                            continue
                        
                    globals()[Nameof_Player].Raise(Val_Raise_Bet)
                    
                    if globals()[Nameof_Player].total_chips < 0:
                        PlayerNames.remove(Nameof_Player)
                        return [f'{Nameof_Player} Folded due to lack of chips']
                    else:
                        return [f'{Nameof_Player} Raised bet to {Val_Raise_Bet}', Val_Raise_Bet]
                    
                else:                                   #####Prints the users cards
                    print('Your Hand '+colored(Nameof_Player, 'yellow', attrs=['bold'])+':')
                    Users_Hand = PlayerCards_dict[Nameof_Player]
                    PrintCards(Users_Hand)
                    Users_Path = 'None'
                    
            else:  #Fold, Bet, Check
                if Users_Path == 'A' or Users_Path == 'a': ##### fold
                    if Nameof_Player in PlayerNames:
                        globals()[Nameof_Player].Fold()
                        RoundNames.remove(Nameof_Player)
                        PlayerCards_dict.pop(Nameof_Player)
                        return [f'{Nameof_Player} Folded','F']
                    
                elif Users_Path == 'B' or Users_Path == 'b': ##### Bet
                    z = False
                    Val_set_Bet = 0
                    while isinstance(Val_set_Bet, int) != True or z != True:  ####This determines how many playes are there
                        Val_set_Bet = input('What is the amount you start the bet to?: ')
                        try:
                            Val_set_Bet = int(Val_set_Bet)
                            if Val_set_Bet > 0:
                                z = True
                            else:
                                continue
                        except:
                            continue
                    globals()[Nameof_Player].Bet(Val_set_Bet)    
                    if globals()[Nameof_Player].total_chips < 0:
                        PlayerNames.remove(Nameof_Player)
                        return [f'{Nameof_Player} Folded due to lack of chips']
                    else:
                        return [f'{Nameof_Player} started betting at: {Val_set_Bet}', Val_set_Bet]
                    
                elif Users_Path == 'C' or Users_Path == 'c':           ##### Check
                    return [f'{Nameof_Player} checked']
                
                else:                                   #####Prints the users cards
                    print('Your Hand '+colored(Nameof_Player, 'yellow', attrs=['bold'])+':')
                    Users_Hand = PlayerCards_dict[Nameof_Player]
                    PrintCards(Users_Hand)
                    Users_Path = 'None'
                
            
def Round_Ender(Roundnames):
    li = []
    for Nameof_Player in Roundnames:
        Amount_bet = globals()[Nameof_Player].CurrentBet
        li.append(Amount_bet)
    if len(set(li)) == 1:
        return False
    else:
        return True




###Intro
print('\n'*35)
print('\nYou will soon learn there are many different variations of Poker, but the one thing they have in common is that you have to use the best five cards to make your hand. All forms of poker use a fifty two card deck made up of of ranks starting with a 2, commonly called deuce, and continuing by numbers until 10 and then in order comes the Jack, Queen, King, and Ace. There are four different Suits; Spades;♠, Hearts; ♥, Diamonds; ♦, and Clubs; ♣,all of which are equal of value in Poker. So four different Suits of 13 different ranks make the 52 cards in a complete deck.')

sleep(3)

####OBJ
print('\nThe objective of poker is very simple – to win the money in the centre of the table, called the pot, which contains the sum of the bets that have been made by the participants of that hand. Players make their bets or wagers on the belief they have the best hand or in the hopes they can make a better hand give up, abdicating the pot to them.')

print('\nIf you do not know how to play Poker Texas Hold `Em Style the following link will guide you to a quick rundown on how to play Poker:\n\nhttps://www.youtube.com/watch?v=GAoR9ji8D6A&ab_channel=PokerVIP')

input('Press Anything to continue.')

running = 0
PlayerNames = []
PlayerCards_li = []
NumPlayers = ''
idx = 0
z = False
print('\n'*35)
while isinstance(NumPlayers, int) != True or z != True:  ####This determines how many playes are there
    NumPlayers = input('How many players is there?: (4-10)  ')
    try:
        NumPlayers = int(NumPlayers)
        if NumPlayers > 2 and NumPlayers < 9:
            z = True
        else:
            continue
    except:
        continue
    
runs = 0
z = False
sleep(0.5)

while isinstance(runs, int) != True or z != True:  ##How many times do they want to play
    runs = input('How many times does your group want to play?:  ')
    try:
        runs = int(runs)
        if runs > 0:
            z = True
        else:
            continue
    except:
        continue
NumChips = 0
z = False
sleep(0.5)

while isinstance(NumChips, int) != True or z != True:  ##How many chips shall be assigned to each player
    NumChips = input('How many'+colored(' chips ', 'red', attrs=['bold'])+'shall be assigned to each player?: MIN(300) ')
    try:
        NumChips = int(NumChips)
        if NumChips >= 300:
            z = True
        else:
            continue
    except:
        continue
    
sleep(0.5)
    
print('\n'+colored('Chips', 'red', attrs=['bold'])+' have been determined')
sleep(1)

for player in range(1,NumPlayers+1):  #####This determines the playes's names
    Names = input(f'Player {player} what is your name: ')
    PlayerNames.append(Names)
    
    
for name in PlayerNames:
        globals()[name] = Player(NumChips)   




print('\n'+colored('Chips', 'red', attrs=['bold'])+' have been assigned')
sleep(3)

# =============================================================================
# 
# =============================================================================

while running <= runs:
    print('\n'*39)
    print(f'\nGAME {running + 1}')
    sleep(2)
    print('')
    for name in PlayerNames:
        print(colored(name, 'yellow', attrs=['bold']),globals()[name])
        sleep(1)
        
    CreateDeck()
    sleep(1)
    print('\nDeck has been created and Shuffled')
    
    PlayerCards_dict = {}
    
    Community_Cards = []
    
    The_Pot = 0
    
    RoundNames = []
    
    for name in PlayerNames:
        RoundNames.append(name)
        
    for eachplayer in range(len(RoundNames)): ######This will deal two cards to each player & assign the chips for the rest of the game
        li = []
        for u in range(2):
            Card_pop = CardDeck.pop()
            li.append(Card_pop)
        PlayerCards_li.append(li)
    sleep(1)
    print('\nCards have been dealt')
    
    for name, hand in zip(RoundNames,PlayerCards_li):
        PlayerCards_dict[name] = hand
    
    
    TheDealer = RoundNames[idx]  #This determines who is the SB and the BB
    idx = (idx + 1) % len(RoundNames)
    TheSmallBlind = RoundNames[idx]
    idx = (idx + 1) % len(RoundNames)
    TheBigBlind = RoundNames[idx]
    sleep(1)
    print('\nThe Dealer this game will be:', colored(TheDealer, 'yellow', attrs=['bold']))
    sleep(1)
    print('\nThe Small Blind is:', colored(TheSmallBlind, 'yellow', attrs=['bold']))
    sleep(1)
    print('\nThe Big Blind is:',colored(TheBigBlind, 'yellow', attrs=['bold']))
    
    THE_PRE_FLOP = False
    THE_FLOP = False
    THE_TURN = False
    THE_RIVER = False
    THE_SHOWDOWN = False
    
    Currnt_Highest_Bet = 0
    k = False
    The_Pot = 0
    
    ListofActions = []
    
    sleep(2)
# =============================================================================
#     
# =============================================================================
    
    THE_PRE_FLOP = True
    SB = 0
    BB = 0
    print('\n'*35)
    print('The '+ colored('PRE-FLOP', 'cyan', attrs=['bold']) +' round will soon begin')
    sleep(3)
    # THE PRE-FLOP - SB AND BB PLACE THEIR BETS AND A NORMAL ROUND OF BETTING BEGINS
    while THE_PRE_FLOP != False:
        
        SB_Bet_Val = set_SB_Bet(SB)
        BB_Bet_Val = set_BB_Bet(BB,SB_Bet_Val)
         
        globals()[TheSmallBlind].SmallBlind(SB_Bet_Val)
        globals()[TheBigBlind].BigBlind(BB_Bet_Val)
    
        Currnt_Highest_Bet = BB_Bet_Val
        
        while THE_PRE_FLOP != False:
            if len(RoundNames) == 1:
                THE_PRE_FLOP = False
                break
            print('\n'*35)
            idx = (idx + 1) % len(RoundNames)
            Current_Player_Turn = RoundNames[idx]
            
            sleep(1)
            print('\n\n'+colored(Current_Player_Turn, 'yellow', attrs=['bold'])+' it is your turn')
            sleep(1)
            print('')
            print(colored(Current_Player_Turn, 'yellow', attrs=['bold']),globals()[Current_Player_Turn])

            
            sleep(1)
            print('\nThe Pot:',The_Pot)
            sleep(1)
            print('\n'+colored('Current Highest Bet: ', 'blue', attrs=['bold'])+f'{Currnt_Highest_Bet}')
            try:
                sleep(1)
                print('\nActions:')
                for action in ListofActions:
                    sleep(0.5)
                    print(f'{action}')
            except:
                print('\nNone')
            
            sleep(2)
            Actions_Results = Turn_Options(Current_Player_Turn,Currnt_Highest_Bet)
            ListofActions.append(Actions_Results[0])
            try:
                if Actions_Results[1] == 'F':
                    idx = (idx - 1) % len(RoundNames)
                if Actions_Results[1] != 'F':
                    Currnt_Highest_Bet = Actions_Results[1]
            except:
                pass
            
            if Currnt_Highest_Bet > 0:
                THE_PRE_FLOP = Round_Ender(RoundNames)
#-------------------------------------------------------------------------------          
    for name in RoundNames:
        globals()[name].endofRound()
        
    The_Pot += Currnt_Highest_Bet*len(RoundNames)
    Currnt_Highest_Bet = 0
#-------------------------------------------------------------------------------
    
    idx = 0
    THE_FLOP = True   
    ListofActions = [] 
    print('\n'*35)
    print('The '+ colored('FLOP', 'cyan', attrs=['bold']) +' round will soon begin')
    sleep(3)    
    # THE FLOP - *3 COMMUNITY CARDS* ARE REVEALED & ANOTHER ROUND OF BETTING BEGINS
    while THE_FLOP != False:
        
        for x in range(3):
            Card_pop = CardDeck.pop()
            Community_Cards.append(Card_pop)
            
        while THE_FLOP != False:
            if len(RoundNames) == 1:
                 THE_FLOP = False
                 break
                 
            print('\n'*35)
            
            idx = (idx + 1) % len(RoundNames)
            Current_Player_Turn = RoundNames[idx]
            sleep(1)
            print('\nCommunity Cards:')
            PrintCards(Community_Cards)
            sleep(1)
            print('\n\n'+colored(Current_Player_Turn, 'yellow', attrs=['bold'])+' it is your turn')
            sleep(1)
            print('')
            print(colored(Current_Player_Turn, 'yellow', attrs=['bold']),globals()[Current_Player_Turn])

            sleep(1)
            print('\nThe Pot:',The_Pot)
            sleep(1)
            print('\n'+colored('Current Highest Bet: ', 'blue', attrs=['bold'])+f'{Currnt_Highest_Bet}')
            try:
                sleep(1)
                print('\nActions:')
                for action in ListofActions:
                    sleep(0.5)
                    print(f'{action}')
            except:
               print('\nNone')
            
            sleep(2)
            
            Actions_Results = Turn_Options(Current_Player_Turn,Currnt_Highest_Bet)
            ListofActions.append(Actions_Results[0])
            try:
                if Actions_Results[1] == 'F':
                    idx = (idx - 1) % len(RoundNames)
                if Actions_Results[1] != 'F':
                    Currnt_Highest_Bet = Actions_Results[1]
            except:
                pass
            
            if Currnt_Highest_Bet > 0:
                THE_FLOP = Round_Ender(RoundNames)
#-------------------------------------------------------------------------------          
    for name in RoundNames:
        globals()[name].endofRound()
        
    The_Pot += Currnt_Highest_Bet*len(RoundNames)
    Currnt_Highest_Bet = 0
#-------------------------------------------------------------------------------

    idx = 0
    THE_TURN = True  
    ListofActions = [] 
    print('\n'*35)
    print('The '+ colored('TURN', 'cyan', attrs=['bold']) +' round will soon begin')
    sleep(3)                  
    # THE TURN - *THE FOURTH COMMUNITY CARD* IS REVEALED & NORMAL ROUND OF BETTING BEGINS
    while THE_TURN != False:
        
        Card_pop = CardDeck.pop()
        Community_Cards.append(Card_pop)
            
        while THE_TURN != False:
            if len(RoundNames) == 1:
                THE_TURN = False
                break
                
            print('\n'*35)
            
            idx = (idx + 1) % len(RoundNames)
            Current_Player_Turn = RoundNames[idx]
            sleep(1)
            print('\nCommunity Cards:')
            PrintCards(Community_Cards)
            sleep(1)
            print('\n\n'+colored(Current_Player_Turn, 'yellow', attrs=['bold'])+' it is your turn')
            sleep(1)
            print('')
            print(colored(Current_Player_Turn, 'yellow', attrs=['bold']),globals()[Current_Player_Turn])

            sleep(1)
            print('\nThe Pot:',The_Pot)
            sleep(1)
            print('\n'+colored('Current Highest Bet: ', 'blue', attrs=['bold'])+f'{Currnt_Highest_Bet}')
            try:
                sleep(1)
                print('\nActions:')
                for action in ListofActions:
                    sleep(0.5)
                    print(f'{action}')
            except:
                print('\nNone')
            
            sleep(2)
            
            Actions_Results = Turn_Options(Current_Player_Turn,Currnt_Highest_Bet)
            ListofActions.append(Actions_Results[0])
            try:
                if Actions_Results[1] == 'F':
                    idx = (idx - 1) % len(RoundNames)
                if Actions_Results[1] != 'F':
                    Currnt_Highest_Bet = Actions_Results[1]
            except:
                pass
               
            if Currnt_Highest_Bet > 0:
                print('entered Round_Ender')
                THE_TURN = Round_Ender(RoundNames)
                print('result:',THE_TURN)
#-------------------------------------------------------------------------------          
    for name in RoundNames:
        globals()[name].endofRound()
        
    The_Pot += Currnt_Highest_Bet*len(RoundNames)
    Currnt_Highest_Bet = 0
#-------------------------------------------------------------------------------
    
    idx = 0
    THE_RIVER = True
    ListofActions = []
    print('\n'*35)
    print('The '+ colored('RIVER', 'cyan', attrs=['bold']) +' round will soon begin')
    sleep(3)
    # THE RIVER - *THE FIFTH COMMMUNITY CARD* IS REVEALED & FINAL ROUND OF BETTING BEGINS (SAME RULES APPLY)
    while THE_RIVER != False:
        
        Card_pop = CardDeck.pop()
        Community_Cards.append(Card_pop)
            
        while THE_RIVER != False:
            if len(RoundNames) == 1:
                THE_RIVER = False
                break
            
            print('\n'*35)
            
            idx = (idx + 1) % len(RoundNames)
            Current_Player_Turn = RoundNames[idx]
            sleep(1)
            print('\nCommunity Cards:')
            PrintCards(Community_Cards)
            sleep(1)
            print('\n\n'+colored(Current_Player_Turn, 'yellow', attrs=['bold'])+' it is your turn')
            sleep(1)
            print('')
            print(colored(Current_Player_Turn, 'yellow', attrs=['bold']),globals()[Current_Player_Turn])

            sleep(1)
            print('\nThe Pot:',The_Pot)
            sleep(1)
            print('\n'+colored('Current Highest Bet: ', 'blue', attrs=['bold'])+f'{Currnt_Highest_Bet}')
            try:
                sleep(1)
                print('\nActions:')
                for action in ListofActions:
                    sleep(0.5)
                    print(f'{action}')
            except:
                print('\nNone')
            
            sleep(2)
            
            Actions_Results = Turn_Options(Current_Player_Turn,Currnt_Highest_Bet)
            ListofActions.append(Actions_Results[0])
            try:
                if Actions_Results[1] == 'F':
                    idx = (idx - 1) % len(RoundNames)
                if Actions_Results[1] != 'F':
                    Currnt_Highest_Bet = Actions_Results[1]
            except:
                pass
            
            if Currnt_Highest_Bet > 0:
                print('entered Round_Ender')
                THE_RIVER = Round_Ender(RoundNames)
                print('result:',THE_RIVER)
               
#-------------------------------------------------------------------------------          
    for name in RoundNames:
        globals()[name].endofRound()
        
    The_Pot += Currnt_Highest_Bet*len(RoundNames)
    Currnt_Highest_Bet = 0
#-------------------------------------------------------------------------------
    print('\n'*35)
    print('The '+ colored('SHOWDOWN', 'red', attrs=['bold']) +' round will soon begin')
    sleep(3)
    # THE SHOWDOWN - EVERYONE REVEALS THEIR CARDS AND THE WINNER IS DETERMINED
    def Best_Five_Card_Poker(Player_Hand, Communitty_Cards):
        Five_Card_Value = 0
        Current_best = ''
        Function_li = [Royal_Flush,Straight_Flush,FOAK,Full_House,Flush,Straight,TOAK,Two_Pairs,One_Pairs,High_Card]
        
        All_Cards = Player_Hand + Communitty_Cards
        comb = combinations(list(All_Cards),5)
        for Five_Cards in list(comb):
            for Function in Function_li:
                Expected_Val = Function(Five_Cards)
                if Expected_Val[0] > Five_Card_Value:
                    Five_Card_Value = Expected_Val[0]
                    Current_best = Expected_Val
                    
        return Current_best
        
    Hand_Val = []
    Best_Cards = []
    Name_Val = []
    for user_hand in PlayerCards_dict:
        Player_Hand = Best_Five_Card_Poker(PlayerCards_dict[user_hand], Community_Cards)
        Hand_Val.append(Player_Hand[0])
        Best_Cards.append(Player_Hand[1])
        Name_Val.append(Player_Hand[2])
    
    Final_Card_Value = {}
    Final_Name_Cards = {}
    Final_Hand_Name_Value = {}
    
    for Name_Value,Player_Names in zip(Name_Val,RoundNames):
        Final_Hand_Name_Value[Player_Names] = Name_Value
    
    for Val_Hand,Player_Names in zip(Hand_Val,RoundNames):
        Final_Card_Value[Player_Names] = Val_Hand
    
    for Cards,Player_Names in zip(Best_Cards,RoundNames):
        Final_Name_Cards[Player_Names] = Cards
    
    max_key = max(Final_Card_Value, key= Final_Card_Value.get)
    listOfKeys = []
    for key, value in Final_Card_Value.items():
        if value == Final_Card_Value[max_key]:
            listOfKeys.append(key)
    
    if len(listOfKeys) == 1:
        U = Final_Hand_Name_Value[max_key]
        print('The Winner is: ')
        sleep(2)
        print(colored(max_key, 'yellow', attrs=['bold']),'\nwith '+U+':')
        sleep(2)
        PrintCards(Final_Name_Cards[max_key])
        globals()[max_key].Win(The_Pot)
        sleep(2)
        print('\n'+colored(max_key, 'yellow', attrs=['bold'])+' you now have:',globals()[max_key].total_chips,colored(' chips', 'red', attrs=['bold']))
        
    else:
        print('The Winners are:')
        for Name_ in listOfKeys:
            U = Final_Hand_Name_Value[Name_]
            print('\n')
            sleep(2)
            globals()[Name_].Winners(The_Pot,len(listOfKeys))
            print(colored(Name_, 'yellow', attrs=['bold'])+' with '+U+':')
            PrintCards(Final_Name_Cards[Name_])
            sleep(2)
            print('\n'*4)
        for Name_ in listOfKeys:
            sleep(1)
            print('\n'+colored(Name_, 'yellow', attrs=['bold'])+ ' you now have:',globals()[Name_].total_chips,colored(' chips', 'red', attrs=['bold']))
   
    running += 1        
    idx = (idx + running) % len(PlayerNames)

    
    if running == runs:
        print('\nThanks for Playing!')
        sleep(1)
        extra = 0
        z = False
        while isinstance(extra, int) != True or z != True: ##If the users wish to keep playing
            extra = input('\nIf you want to continue playing just enter the number of extra games you want to play.\nIf you wish to exit just enter 0.\n\nAnswer: ')
            try:
                extra = int(extra)
                if extra >= 0:
                    z = True
                else:
                    continue
            except:
                continue
        
        if extra == 0:
            break
        else:
            runs += extra
    else:
        input('\nPress anything to continue')
        
print('\n'*35)
print('Thanks for Playing!')
    