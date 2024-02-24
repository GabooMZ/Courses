# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:43:12 2021

@author: Gabriel Melendez
"""

'''

GUI

Graphic User Interface

by Gabriel M
'''

from tkinter import *

root = Tk()


e = Entry(root,width= 50,borderwidth=5,lenght=100)
e.pack()


def myClick():
    myLabel = Label(root, text = 'Look I clicked a Button!').pack()


myLabel = Label(root, text='Hello World').pack()

myButton = Button(root, text = 'Click Me!', command=myClick,fg='blue',bg='#000000').pack()




root.mainloop()