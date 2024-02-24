# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:24:19 2020

@author: Gabriel Melendez
"""


#%%

'''

HW_10_Pirple 

Importing

by Gabriel M
'''

import calendar
m =('-'*40)

#The following function determines if the given year is a leap year or not.
print('calendar.isleap(year)')

year = 2020
a = calendar.isleap(year)

print(year)
print(a)
print(m)
# =============================================================================
# %%
# =============================================================================

#The following function determines how many leap years are there in the range of the 2 given years.
print('\ncalendar.leapdays(y1, y2)')

y1 = 2010
y2 = 2020
a = calendar.leapdays(y1,y2)

print(y1,y2)
print(a) 
print(m)
# =============================================================================
# %%
# =============================================================================

#The following function Returns the day of the week.
#the day given must be between 1-31.
#The return value is between 0-6, 0 for Monday and 6 for Sunday.
print('\ncalendar.weekday(year, month, day)')

year = 2020
month = 12
day = 7
a = calendar.weekday(year, month, day)

print(year,month,day)
print(a)
print(m)
# =============================================================================
# %%
# =============================================================================

#The following function sets the first weekday 0-6 (0=Monday, 6=Sunday).
print('\ncalendar.setfirstweekday(weekday)')

weekday = 0
a = calendar.setfirstweekday(weekday)

print(weekday)
print(a)
print(m)
# =============================================================================
# %%
# =============================================================================

#The following function return a header containing abbreviated weekday names.
#The order can vary according to -> calendar.setfirstweekday(weekday).^^^^^^^^
# n corresponds to the width between each value
print('\ncalendar.weekheader(n)')

n = 3
a = calendar.weekheader(n)

print('The width is:',n)
print(a)
print(m)
# =============================================================================
# %%
# =============================================================================

#The following function returns weekday of first day of the month (0=Monday, 6=Sunday)
#And number of days in month, for the specified year and month.
print('\ncalendar.monthrange(year, month)')

year = 2020
month = 12
a = calendar.monthrange(year, month)

print(year,month)
print(a)
print(m)
# =============================================================================
# %%
# =============================================================================

#The following function returns a matrix representing a month’s calendar.
#Each row represents a week.
#Each week begins with Monday unless set by -> setfirstweekday().
#Days outside of the month are represented by zeros
print('\ncalendar.monthcalendar(year, month)')

year = 2020
month = 12
a = calendar.monthcalendar(year, month)

print(year,month)
print(a)
print(m)
# =============================================================================
# %%
# =============================================================================

#The following function returns a month’s calendar in a multi-line string 
print('\ncalendar.month(theyear, themonth, w=0, l=0)')

theyear = 2009
themonth = 8
a = calendar.month(theyear, themonth, w=0, l=0)

print(theyear,themonth)
print(a)
print(m)
# =============================================================================
# %%
# =============================================================================

#Returns a 3-column calendar for an entire year
#w and l represent the width between each word and lenght between each line *(w&l -= 1)*
#c = sapce between months
#m = how many columns of months do you want
print('calendar.calendar(year, w=2, l=1, c=6, m=3)')

year = 2012
a = calendar.calendar(year, w=2, l=1, c=6, m=3)

print(year)
print(a)
print(m)
# =============================================================================
# %%
# =============================================================================