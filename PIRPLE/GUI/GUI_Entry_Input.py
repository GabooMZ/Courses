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


e = Entry(root,width= 50,borderwidth=5)
e.pack()
e.insert(0,'Enter your Name')


def myClick():
    hello = 'Hello '+ e.get()
    myLabel = Label(root, text = hello).pack()


myButton = Button(root, text = 'Enter your Name', command=myClick,fg='blue',bg='#000000').pack()




root.mainloop()