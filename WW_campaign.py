# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:11:32 2019

@author: owner
"""
import WW_classes
import WW_items
from random import randint
import numpy as np


def newGame():
    global plyr
    plyr_class = ""
    while plyr_class not in ['1', '2']:
        plyr_class = input("Choose class, enter(1) for Wizard and (2) for Warrior:")
    name = ""
    while len(name) == 0:
        name = input("Name your character: ")
    plyr_class = WW_classes.classes[int(plyr_class)]
    if plyr_class == "Wizard":
        plyr = WW_classes.Wizard(name)
    if plyr_class == "Warrior":
        plyr = WW_classes.Warrior(name)
    plyr.name = name
    plyr.clss = plyr_class
    story()
    
    
def show_stats(char):
    if char.clss not in WW_classes.classes.values():
        print("\n", char.clss, "|", "HP:", char.hp)
    else:
        print("\n", char.name, "|", char.clss, "|", "HP:", char.hp, "|", "MP:", char.mp, "|", "Dmg:", char.dmg, "|", "Block:", char.block)
        cats = ['skills', 'equipment', 'inventory']
        for cat in cats:
            items = []
            char_cat = getattr(char, cat)
            for e in char_cat:
                if cat == 'skills':
                    items.append([f" {e.name}, {e.typ}:{e.stat}, Mana Cost:{e.mana_cost}, Cool Down:{e.cool_down}"])
                elif cat == 'equipment':
                    items.append([f" {e.name}, {e.typ}:{e.stat}"])
                elif cat == 'inventory':
                    items.append([f" {e.name}, {e.typ}:{e.stat}"])
            print(f"{cat.capitalize()}: {items}")
        
def loot():
    loot_item = np.random.choice(WW_items.items)
    WW_items.item_info(loot_item)
    pick_up = ""
    while pick_up.upper() not in ['Y', 'C']:
        pick_up = input(f"Enter (Y) to equip {loot_item['name']}, or (C) to cancel:")
    if pick_up.upper() == 'Y':
        item = WW_items.Item(loot_item)
        for key in loot_item:
            setattr(item, key, loot_item[key])
        equip(item)
    elif pick_up.upper() == 'C':
        pass

        
    
    
def equip(item):
    plyr_cat = getattr(plyr, item.cat)
    if len(plyr_cat) == 2:
        swap(item)
    else:
        if item.cat == 'skills':
            if item.clss == plyr.clss:
                plyr_cat.append(item)
            else: 
                print("\n" + "Wrong class")
        elif item.cat == 'equipment':
            if item.clss == plyr.clss:
                print("25% bonus for matching class.")
                item.stat *= 1.25
            setattr(plyr, item.typ, getattr(plyr, item.typ) + item.stat)
            plyr_cat.append(item)
        elif item.cat == 'inventory':
            plyr_cat.append(item)  
    show_stats(plyr)
    
    
    
def use(item):
    plyr_cat = getattr(plyr, item.cat)
    setattr(plyr, item.typ, getattr(plyr, item.typ) - item.stat)
    plyr_cat.remove(item)
    

def swap(item):
    print("\n" + "Only two items can fit in this slot.")
    plyr_cat = getattr(plyr, item.cat)
    plyr_cat_copy = plyr_cat.copy()
    for e in plyr_cat_copy:
        to_swap = input("Enter (1) to swap out " + e.name + ", Enter (C) to cancel:")
        if to_swap == '1':
            if item.cat == 'equipment':
                use(e)
            else:
                plyr_cat.remove(e)
            equip(item)
            break
    print("\n" + "No items left")              
    

    
def battle(enemy):
    print("\n", "Enemy encountered!")
    show_stats(enemy)
     
 
    
         
def roll(die):
    return randint(1, die)
   
             

###STORY###
def story():
    loot()
    battle(WW_classes.Goblin('Goblin'))
    
    
newGame()

    

    
            