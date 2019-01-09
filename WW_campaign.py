# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:11:32 2019

@author: owner
"""
import WW_classes

def newGame():
    classes = {1: "Wizard", 2: "Warrior"}
    plyr_class = int(input("Choose class: enter(1) for Wizard and (2) for Warrior."))
    if plyr_class not in classes.keys():
        return newGame()
    name = input("Name your character: ")
    if plyr_class == 1:
        name = WW_classes.Wizard(name)
    if plyr_class == 2:
        name = WW_classes.Warrior(name)
   
        
    
        
newGame()
            