# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:38:08 2020

@author: Laura & Johannes
"""

import resolution

def all_sets(s):
    '''
    This function calculates all possible subsets given a list.
    ''' 
    x = len(s)
    ls = []
    for i in range(1 << x):
        ls.append([s[j] for j in range(x) if (i & (1 << j))])
    return ls

def final_subsets(li):
    '''
    This function takes a list of logical sentences as input and returns a list
    of the largest subsets from the list.
    '''
    index = []
    for i in range(len(li)):    
        for j in range(len(li)):  
            if i != j:         
                if li[i].issubset(li[j]):
                    index.append(i)                     
    index = list(set(index))

    C_prime = []
    for i in range(len(li)):
        if i not in index:
            C_prime.append(li[i])
            
    return C_prime
            
def consist_check(C_list, formula):
    '''
    This function checks whether the logical sentences from C_list is consistent
    with the new belief (formula). In order to make this consistency check the 
    resolution function is used. It returns all the sentences from C_list which
    are consistent with the new belief.
    '''
    ls = []
    for i in C_list:
        if len(i) > 0:
            res = set(i)
            if (resolution.resolution_check(res, formula)) == False:
                ls.append(set(i))
    
    return ls

def selection(bb, rev, formula, formula_order):   
    '''
    This function takes the following inputs:
        1) bb, the belief base
        2) rev, the remainders found by revision of belief base
        3) formula, the new belief
        4) formula_order, the order of the new belief
    It returns the belief base which only contains the remainder with highest
    order as well as the new belief.
    '''   
    
    # Find index of remainders that should not be kept in belief base
    ind = []
    for i in rev:
        ls = list(i)
        num = 0
        for j in ls:
            num += bb[j]          
        ind.append(num/len(ls))        
    pos = ind.index(max(ind))    
    d = rev[pos]     
    keys_to_remove = list(set(bb)-d)
    
          
    # Remove raminders that should not be kept in belief base
    for key in keys_to_remove:
      bb.pop(key)
        

    # Add new belief to belief base
    bb[formula] = formula_order
    
    return bb


def revise(beliefbase, formula, order):
    '''
    This function takes the belief base as well as the new input (formula) as 
    input and returns a list of subsets that are candidates to be retained in the
    beliefbase together with the new belief.
    '''  
    # Turn beliefbase to list 
    bb = list(set(beliefbase.keys()))
    
    # Find all subsets of beliefbase
    C_sub = all_sets(bb)
    
    # Find all subsets of beliefbase which are consistent with the new belief (formula)    
    c = consist_check(C_sub, formula)
    
    # Find a list of the largest subset among the subsets that are consistent with beliefbase
    C_prime = final_subsets(c)
    
    # If no beliefs from the belief base is consistent with new belief, 
    # update belief base to contain only the new belief. Else use selection function
    # to select among remainders to keep in belief base together with the new belief
    if len(C_prime) == 0:
        bb = {formula: order}
    
    else:
        bb = selection(beliefbase, C_prime, formula, order) 
    
    return bb
    
