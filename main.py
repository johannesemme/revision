# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:49:24 2020

@author: Laura & Johannes
"""
import ui
import resolution
import revision
import logic
from sympy.logic.boolalg import to_cnf

class BeliefBase:
    def __init__(self):
        '''
        Initialization of belief base
        '''
        self.beliefs = {}
    
    def add(self, newbelief, order):
        '''
        This function adds the new belief to the belief base and displays 
        the updated belief base.
        '''
        
        # If new belief is inconsistent with belief base 
        if resolution.resolution_check(set(self.beliefs.keys()),newbelief):
                      
            # Making revision to update belief base so that it contains the 
            # 'right' remainders and the new belief
            self.beliefs = revision.revise(self.beliefs,newbelief, order )

        # If new belief is not inconsistent with beleif base, add it to the belief base
        else:
            self.beliefs[newbelief] = order

        # Display belief base after update
        self.display_beliefbase()
        
    def clear_beliefbase(self):
        '''
        This function clears the belief base
        '''
        self.beliefs.clear()
        
        print("\nBelief base: ")
        print(self.beliefs)
        
        
    def display_beliefbase(self):
        '''
        This function displays the belief base
        '''
        print("\nBelief base: ")
        print(self.beliefs)
        
    def input_handler(self):
        '''
        This function handles the input from the user
        '''
               
        while True:
            print('\n------- MENU -------')
            menu_choice = ui.displayMenu(['Add new belief','Print belief base','Empty belief base','Quit'],"Choose from the menu: ")        
        
            # Adding new belief
            if menu_choice == 1: 
                
                new_belief = input("Write belief: ")
                while logic.check(new_belief) == False:
                    print('Please input a valid logical argument')
                    new_belief = input("Write belief: ")
                
                weight = float(input("Assign priority (real number betweeen 0 and 1): "))
                while (weight < 0) or (weight > 1):
                    print('Please input a priority between 0 and 1')
                    weight = float(input("Assign priority (real number betweeen 0 and 1): "))
                
                # Convert input belief to CNF-form
                new_belief = to_cnf(new_belief)
                       
                # Adding new belief to belief base
                self.add(new_belief, weight)
                                
            # Printing belief base
            elif menu_choice == 2:                
                self.display_beliefbase()
                
            # Clear the belief base
            elif menu_choice == 3: 
                self.clear_beliefbase()
              
            # Exit the program
            elif menu_choice == 4: 
                print('See you later!')
                break
                          
def main():        
    bb = BeliefBase()
    bb.input_handler()
    
if __name__ == "__main__":
    main()