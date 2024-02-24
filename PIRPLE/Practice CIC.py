# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 19:11:00 2021

@author: Gabriel Melendez
"""

'''

Chapter 2. 

Input, Processing, and Output 

by Gabriel M
'''

# =============================================================================
# 2. Input, Processing, and Output . . . . . . 11
# Exercise 1. Saying Hello 12
# Exercise 2. Counting the Number of Characters 13
# Exercise 3. Printing Quotes 14
# Exercise 4. Mad Lib 15
# Exercise 5. Simple Math 16
# Exercise 6. Retirement Calculator 17
# =============================================================================
#%%
# Exercise 1. Saying Hello
# So create a program that prompts for your name and prints a greeting using your name.

name = input('What is your name? ')
print('Hello,',name+', nice to meet you')

#%%
# Exercise 2. Counting the Number of Characters 
# Create a program that prompts for an input string and displays output that shows the input string and the number of characters the string contains.

x = input('What is the input string? ')
y = len(x)
print(x,'has',y,'characters.')

#%%
# Exercise 3. Printing Quotes 
# Create a program that prompts for a quote and an author. Display the quotation and author as shown in the example output.

quote = input('What is the quote? ')
author = input('Who said it?' )
print(author,f'says, "{quote}"')

#%%
# Exercise 4. Mad Lib 
# Create a simple mad-lib program that prompts for a noun, a verb, an adverb, and an adjective and injects those into a story that you create.

noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
adjective = input('Enter an adjective: ')
adverb = input('Enter an adverb: ')
print('Do you',verb,'your',adjective,noun,adverb+'? That is hilarious!')

#%%
# Exercise 5. Simple Math 
# Write a program that prompts for two numbers. Print the sum, difference, product, and quotient of those numbers as shown in the example output:

x = int(input('What is the first number? '))
y = int(input('What is the second number? '))

print(x,'+',y,'=',x+y)
print(x,'-',y,'=',x-y)
print(x,'x',y,'=',x*y)
print(x,'/',y,'=',x/y)

#%%
# Exercise 6. Retirement Calculator
# Create a program that determines how many years you have left until retirement and the year you can retire. It should prompt for your current age and the age you want to retire and display the output as shown in the example that follows.

# ?????????????????

#%%
# =============================================================================
# 3. Calculations . . . . . . . . . . 19
# Exercise 7. Area of a Rectangular Room 21
# Exercise 8. Pizza Party 22
# Exercise 9. Paint Calculator 23
# Exercise 10. Self-Checkout 24
# Exercise 11. Currency Conversion 25
# Exercise 12. Computing Simple Interest 26
# Exercise 13. Determining Compound Interest 27
# =============================================================================
#%%
# Exercise 7. Area of a Rectangular Room 21
# Create a program that calculates the area of a room. Prompt the user for the length and width of the room in feet. Then display the area in both square feet and square meters.

l = int(input('What is the length of the room in feet? '))
w = int(input('What is the width of the room in feet? '))
print('You entered dimensions of',l,'feet by',w,'feet.')
feet = l*w
meters = round(feet*0.09290304,3)
print(f'The area is\n{feet} square feet\n{meters} square meters')

#%%
# Exercise 8. Pizza Party 22
# Write a program to evenly divide pizzas. Prompt for the number of people, the number of pizzas, and the number of slices per pizza. Ensure that the number of pieces comes out even. Display the number of pieces of pizza each person should get. If there are leftovers, show the number of leftover pieces.

from math import floor

def pluralization(x):
    if x > 1:
        pluralization = ['pizzas','pieces','are']
    else:
        pluralization = ['pizza','piece','is']
    return pluralization

ppl = int(input('How many people? '))
pizza = int(input('How many pizzas do you have? '))

pluralization = pluralization(pizza)
sliceper = floor((pizza*8)/ppl)
leftover = ((pizza*8)%ppl)
print(ppl,'people with',pizza,pluralization[0])
print('Each person gets',sliceper,pluralization[1],'of pizza.')
print('There',pluralization[2],leftover,'leftover',pluralization[1])

#%%
# Exercise 9. Paint Calculator 23
# Calculate gallons of paint needed to paint the ceiling of a room. Prompt for the length and width, and assume one gallon covers 350 square feet. Display the number of gallons needed to paint the ceiling as a whole number.

from math import ceil

num = int(input('how many square feet do you need to paint? '))
gallons = ceil(num/350)

if gallons > 1:
    pluralization = 'gallons'
else:
    pluralization = 'gallon'
print('You will need to purchase',gallons,pluralization,'of paint to cover',num,'square feet.')

#%%
# Exercise 12. Computing Simple Interest 26
# Create a program that computes simple interest. Prompt for the principal amount, the rate as a percentage, and the time, and display the amount accrued (principal + interest).

P = float(input('Enter the principal: '))
r = float(input('Enter the rate of interest: '))
R = r/100 
t = float(input('Enter the number of years: '))
A = (1 + R*t)*P
print('After',t,'years at',r,'%, the investment will be worth $'+str(A))

#%%
# =============================================================================
# 4. Making Decisions . . . . . . . . 29
# Exercise 14. Tax Calculator 33
# Exercise 15. Password Validation 34
# Exercise 16. Legal Driving Age 35
# Exercise 17. Blood Alcohol Calculator 36
# Exercise 18. Temperature Converter 37
# Exercise 19. BMI Calculator 38
# Exercise 20. Multistate Sales Tax Calculator 39
# Exercise 21. Numbers to Names 40
# Exercise 22. Comparing Numbers 41
# Exercise 23. Troubleshooting Car Issues 42
# =============================================================================
#%%
# Exercise 14. Tax Calculator 33
# Write a simple program to compute the tax on an order amount. The program should prompt for the order amount and the state. If the state is “WI,” then the order must be charged 5.5% tax. The program should display the subtotal, tax, and total for Wisconsin residents but display just the total for non-residents.

amount = int(input('What is the order amount? '))
state = input('What is the state? ')
total = amount
if state == 'WI':
    total = amount*1.055
    print('The subtotal is $'+str(amount))
    print('The Tax is:',amount*.055)
print('The total is $',total)

#%%
# Exercise 15. Password Validation 34
# Create a simple program that validates user login credentials. The program must prompt the user for a username and password. The program should compare the password given by the user to a known password. If the password matches,the program should display “Welcome!” If it doesn’t match, the program should display “I don’t know you.”

while True:
    psswrd = input('What is the password? ')
    
    if psswrd == 'zsw123#':
        print('Welcome!')
        break
    else:
        print('I do not know you.')

#%%
# Exercise 16. Legal Driving Age 35
# Write a program that asks the user for their age and compare it to the legal driving age of sixteen. If the user is sixteen or older, then the program should display “You are old enough to legally drive.” If the user is under sixteen, the program should display “You are not old enough to legally drive.”

age = int(input('What is your age? '))

value = 'You are old enough to legally drive.' if age >= 16 else 'You are not old enough to legally drive.'
print(value)

#%%
# Exercise 17. Blood Alcohol Calculator 36
# Create a program that prompts for your weight, gender, number of drinks, the amount of alcohol by volume of the drinks consumed, and the amount of time since your last drink. Calculate your blood alcohol content (BAC) using this formula
#               BAC = (A × 5.14 /W × r) − .015 × H

W = float(input('What is your weight? (lb) '))
gender = input('What is your gender? ')
r = 0.73 if gender == 'men' else 0.66
num = int(input('number of drinks? '))
V = float(input('Amount of alcohol by volume? (%) '))
A = 12.5*num*(V/100)
H = float(input('time since your last drink? (hours) '))

BAC = (A*5.14/W*r)-.015*H
print('Your BAC is', str(BAC))

final = 'It is not legal for you to drive.' if BAC >= 0.08 else 'It is legal for you to drive.'
print(final)

#%%
# Exercise 18. Temperature Converter 37
# Create a program that converts temperatures from Fahrenheit to Celsius or from Celsius to Fahrenheit. Prompt for the starting temperature. The program should prompt for the type of conversion and then perform the conversion.
# The formulas are:      C = (F − 32) × 5 / 9      and       F = (C × 9 / 5) + 32

def ºF_to_ºC():
    F = int(input('Please enter the temperature in Fahrenheit: '))
    C = (F - 32) * 5/9
    return 'The temperature in Celsius is '+str(C)

def ºC_to_ºF():
    C = int(input('Please enter the temperature in Celsius: '))
    F = (C * 9/5) + 32
    return 'The temperature in Fahrenheit is '+str(F)

choice = input('Press C to convert from Fahrenheit to Celsius.\nPress F to convert from Celsius to Fahrenheit.\nYour choice: ')

x = 'Not a valid input'

if choice == 'C' or choice == 'c':
    x = ºF_to_ºC()
elif choice == 'F' or choice == 'f':
    x = ºC_to_ºF()
print(x)

#%%
# Exercise 19. BMI Calculator 38
# Create a program to calculate the body mass index (BMI) for a person using the person’s height in inches and weight in pounds. The program should prompt the user for weight and height.
#               BMI = (weight (kg)/ (height (m))**2)

W = float(input('What is your weight? (kg) '))
h = float(input('What is your height? (m) '))
BMI = (W / (h)**2)

if BMI < 18.5:
    print('You are underweight. You should see your doctor.')
elif BMI > 25:
    print('You are overweight. You should see your doctor.')
else:
    print('You are within the ideal weight range.')
    
#%%
# Exercise 21. Numbers to Names 40
# Write a program that converts a number from 1 to 12 to the corresponding month. Prompt for a number and display the corresponding calendar month, with 1 being January and 12 being December. For any value outside that range, display an appropriate error message.

names = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'Novemeber',12:'December'}
month = int(input('Please enter the number of the month: '))
print('The name of the month is:', names[month])

#%%
# Exercise 22. Comparing Numbers 41
# Write a program that asks for three numbers. Check first to see that all numbers are different. If they’re not different, then exit the program. Otherwise, display the largest number of the three.

first = float(input('Enter the first number: '))

second  = float(input('Enter the second number: '))
while second == first:
    second  = float(input('Enter the second number: '))
    
third = float(input('Enter the third number: '))
while third == second:
    third = float(input('Enter the third number: '))

if first < second:
    if second < third:
        largest = third
    else:
        largest = second
else:
    if first < third:
        largest = third
    else:
        largest = first
print('The largest number is',largest)

#%%
# =============================================================================
# 5. Functions . . . . . . . . . . 45
# Exercise 24. Anagram Checker 47
# Exercise 25. Password Strength Indicator 48
# Exercise 26. Months to Pay Off a Credit Card 49
# Exercise 27. Validating Inputs 51
# =============================================================================
#%%
# Exercise 24. Anagram Checker 47
# Create a program that compares two strings and determines if the two strings are anagrams. The program should prompt for both input strings and display the output as shown in the example that follows.

def isAnagram (first,second):
    l1 = []
    l2 = []
    if len(first) != len(second):
        return f'"{first}" and "{second}" are not anagrams.'
    for first_word_1st_letter, second_word_2nd_letter in zip(first,second):
        l1.append(first_word_1st_letter)
        l2.append(second_word_2nd_letter)
    l1.sort()
    l2.sort()
    if l1 == l2:
        return f'"{first}" and "{second}" are anagrams.'
    else:
        return f'"{first}" and "{second}" are not anagrams.'

print('Enter two strings and I will tell you if they are anagrams: ')
str1 = input('Enter the first string: ')
str2 = input('Enter the second string: ')
print(isAnagram(str1, str2))
#%%
# =============================================================================
# 6. Repetition . . . . . . . . . . 53
# Exercise 28. Adding Numbers 57
# Exercise 29. Handling Bad Input 58
# Exercise 30. Multiplication Table 59
# Exercise 31. Karvonen Heart Rate 60
# Exercise 32. Guess the Number Game 61
# =============================================================================
#%%
# Exercise 28. Adding Numbers 57
# Write a program that prompts the user for five numbers and computes the total of the numbers.

y = 0
for m in range(5):
    x = float(input('Enter a number: '))
    y = y+x
print('The total is',y)

#%%
# Exercise 29. Handling Bad Input 58
# Write a quick calculator that prompts for the rate of return on an investment and calculates how many years it will take to double your investment.

r = ''
z = False
while isinstance(r, float) != True or z != True: 
    r = input('What is the rate of return? ')
    try:
        r = float(r)
        if r > 0:
            z = True
        else:
            print('Sorry. Thats not a valid input.')
            continue
    except:
        print('Sorry. Thats not a valid input.')
        continue
print('It will take',72/r,'years to double your initial investment.')

#%%
# =============================================================================
# 7. Data Structures . . . . . . . . . 63
# Exercise 33. Magic 8 Ball 65
# Exercise 34. Employee List Removal 66
# Exercise 35. Picking a Winner 67
# Exercise 36. Computing Statistics 68
# Exercise 37. Password Generator 70
# Exercise 38. Filtering Values 71
# Exercise 39. Sorting Records 72
# Exercise 40. Filtering Records 73
# What You Learned 74
# =============================================================================
#%%
# Exercise 33. Magic 8 Ball 65
# Create a Magic 8 Ball game that prompts for a question and then displays either “Yes,” “No,” “Maybe,” or “Ask again later.”

from random import shuffle

l1 = ['Yes','No','Maybe','Ask Again Later.']
question = input('What is your question? ')
shuffle(l1)
print(l1[2])    

#%%
# Exercise 34. Employee List Removal 66
# Create a small program that contains a list of employee names. Print out the list of names when the program runs the first time. Prompt for an employee name and remove that specific name from the list of names. Display the remaining employees, each on its own line.

l2 = ['John Smith','Jackie Jackson','Chris Jones','Amanda Cullen','Jeremy Goodwin']
print('There are 5 employees:\nJohn Smith\nJackie Jackson\nChris Jones\nAmanda Cullen\nJeremy Goodwin')
x = input('Enter an employee name to remove: ')
l2.remove(x)
print(f'There are 4 employees:\n{l2[0]}\n{l2[1]}\n{l2[2]}\n{l2[3]}')

#%%
# Exercise 35. Picking a Winner 67
# Create a program that picks a winner for a contest or prize drawing. Prompt for names of contestants until the user leaves the entry blank. Then randomly select a winner.
from random import choice
l1 = []
while True:
    name = input('Enter a name: ')
    if name == '':
        break
    l1.append(name)

winner = choice(l1)
print('The winner is...',winner)

#%%