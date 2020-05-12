# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:31:23 2020

@author: Laura & Johannes
"""

from sympy.logic.boolalg import Or, And

import string

def check(test_str):
    '''
    This function checks if the input is a valid logical sentence
    '''
    allowed = set(string.ascii_uppercase + '&' + ' ' + '|' + '~' + '>>' + '<<' + '(' + ')' + ','+ 'Equivalent')

    if set(test_str) <= allowed:
        return True
    else:
        return False

def conjuncts(s):
    '''
    This function takes a logical sentence as input. If the logical sentence contains 
    conjuncts (&-symbols) the function splits on these conjuncts and return a set of the splitted logical
    sentence. Else it returns the original sentence converted into a list.
    '''
    if isinstance(s, And):
        return s.args
    else:
        return [s]

def disjuncts(s):
    '''
    This function takes a logical sentence as input. If the logical sentence contains 
    disjuncts (|-symbols) the function splits on these disjuncts and return a set of the splitted logical
    sentence. Else it returns the original sentence converted into a list.
    '''
    if isinstance(s, Or):
        return s.args
    else:
        return [s]
