# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:11:32 2019

@author: owner
"""
import WW_classes
import WW_items
from random import randint 


loot_ops = {0: "You found a tresure chest!"}

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
    
def show_stats():
    print(name.name, "|", "Dmg:", name.dmg, "  Block:", name.block, "\n", name.inventory)
    
    
def loot():
    n = len(WW_items.items) - 1
    item = WW_items.items[roll(n)]
    item = WW_items.Stats(item)
    if item.item in WW_items.atk_itms.values():
        print(item.item, "|", "Dmg:", item.stats)
        equip(item, "dmg")
    elif item.item in WW_items.def_itms.values():
        print(item.item, "|", "Block:", item.stats)
        equip(item, "block")
    
    
    
def equip(item, typ):
    pick_up = input("Equip?")
    if pick_up.lower() == "y":
        if typ == "dmg":
            name.dmg += item.stats
        if typ == "block":
            name.block += item.stats
        name.inventory.append(item.item)
    show_stats()
    
         
def roll(n):
    return randint(0, n)
   
              
newGame()

###STORY###
def story():
    loot()
    

    
            