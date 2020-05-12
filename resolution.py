# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:58:31 2020

@author: Laura & Johannes
"""
import itertools
import logic
from sympy.logic.boolalg import to_cnf
from sympy.abc import q

def resolution_check(beliefbase, alpha):
    '''
    This function takes belief base and new belief (alpha) as input and returns 
    'True' if new belief is inconsistent with belief base or 'False' if new belief
    does not violate belief base.
    
    The function is based on the algorithm presented on page 255 (figure 7.12) in
    the book "Artificial Intelligence - A Modern Approach, 3rd edition"
    '''
    
    # Combine belief base and new belief (formula) to a set called 'clauses'
    bb = []
    for i in beliefbase:
        bb.extend(list(logic.conjuncts(i)))
    
    formula = list(logic.conjuncts(alpha))
    #bb = list(beliefbase)
    clauses = set(bb + formula)
        
    # Set of all resolvents
    new = set() 
    
    # Continue resolution of clauses until either inconsistency is detected or not
    while True:
        # Generate all clause pairs
        clause_pairs = []
        
        for belief in itertools.combinations(clauses,2):
            clause_pairs.append(belief)
         
        # Find resolvents for each clause pairs
        for ci, cj in clause_pairs:
            resolvents = resolve(ci, cj)
            
            # If no resolvents new belief is inconsisten with belief base - return 'True'
            if len(resolvents) == 0:
                return True
                break
            
            # Append new resolvents to the 'new'
            new = new.union(set(resolvents))

        # If set of resolvents already exist in clauses (is a subset) then return 'False'
        if new.issubset(clauses):
            return False
              
        # Union clauses with resolvents to get new clauses
        clauses = clauses.union(set(new))

def resolve(ci, cj):
    '''
    This function takes two arguments from a clause pair and returns the resolvents
    ''' 
    
    # Convert each input to a list
    if len(ci.args) <= 1:
        buffer = ci | to_cnf(q)
        ci_list = list(buffer.args)
        ci_list.remove(to_cnf(q))
    else:
        ci_list = list(ci.args)
           
    if len(cj.args) <= 1:
        buffer = cj | to_cnf(q)
        cj_list = list(buffer.args)
        cj_list.remove(to_cnf(q))
    else:
        cj_list = list(cj.args)
        
    # Find index of elements that contradicts and remove these
    index_i = []
    index_j = []
    for i in range(0, len(ci_list)):
        for j in range(0, len(cj_list)):
            if (to_cnf(ci_list[i]) == ~to_cnf(cj_list[j])) or (~to_cnf(ci_list[i]) == to_cnf(cj_list[j])) :               
                index_i.append(i)
                index_j.append(j)       
    ci_list_revised = [l for k,l in enumerate(ci_list) if k not in index_i]
    cj_list_revised = [l for k,l in enumerate(cj_list) if k not in index_j]
    joined_lists = ci_list_revised + cj_list_revised
    
    
    # Secure that there is no redundant element
    unique_list = list(set(joined_lists))
    
    # If no resolvents return empty list, else return list where each element is logically
    # conjuncted with each other
    if len(unique_list) == 0:
        return []

    else:
        res = to_cnf(unique_list[0])
        for i in range(1,len(unique_list)):
            res = to_cnf(res | to_cnf(unique_list[i]))
        return list(logic.conjuncts(res))
    
