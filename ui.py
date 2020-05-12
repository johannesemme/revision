# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:48:48 2020

@author: Laura & Johannes
"""
import numpy as np

def inputNumber(prompt):
    '''
    This function handles input errors.
    '''
    
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Please choose a valid number from the menu")
            pass
    return num
    
def displayMenu(options, text):
    '''
    This function takes two inputs:
        1) Options, which is a list of menu choices
        2) Text, which is the title of the menu
    It then uses these inputs to display a menu that the user can choose from.
    '''
    
    #Prints menu using the list 'options'
    for i in range(len(options)):
        print("{}. {}".format(i+1,options[i]))
        
    #Handles input and displays error if choice is invalid
    choice = 0
    while not choice in np.arange(1,len(options)+1):
        choice = inputNumber(text)
        if choice > len(options) or choice <= 0:
            print("\nInvalid choice")

    return choice


    