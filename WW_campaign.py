# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:11:32 2019

@author: owner
"""
import WW_classes
import WW_items
from random import randint 


def newGame():
    plyr_class = int(input("Choose class, enter(1) for Wizard and (2) for Warrior:"))
    if plyr_class not in WW_classes.classes:
        print("Invalid class.")
        return newGame()
    global name
    name = input("Name your character: ")
    if plyr_class == 1:
        name = WW_classes.Wizard(name)
    if plyr_class == 2:
        name = WW_classes.Warrior(name)
    story()
    
    
def loot():
    n = len(WW_items.items) - 1
    item = WW_items.items[roll(n)]
    item = WW_items.Stats(item)
    pick_up = input("Equip " + item.item + "?")
    if pick_up.lower() == "y":
        name.inventory.append(item.item)
        print(name.inventory)
        print(item.stats)

#def stats():
    

        
def roll(n):
    return randint(0, n)
   
              
newGame()

###STORY###
def story():
    print("You found a tresure chest!")
    loot()
            