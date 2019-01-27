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
    try:
        plyr_class = int(input("Choose class, enter(1) for Wizard and (2) for Warrior:"))
    except:
        print("\n", "Invalid class.")
        return newGame()
    if plyr_class not in WW_classes.classes:
        print("\n", "Invalid class.")
        return newGame()
    name = input("Name your character: ")
    plyr_class = WW_classes.classes[plyr_class]
    if plyr_class == "Wizard":
        plyr = WW_classes.Wizard(name)
    if plyr_class == "Warrior":
        plyr = WW_classes.Warrior(name)
    plyr.name = name
    plyr.clss = plyr_class
    story()
    
    
def show_stats(char):
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
    pick_up = int(input(f"Enter (1) to equip {loot_item['name']} or (P) to pass:"))
    if pick_up == 1:
        item = WW_items.Item(loot_item)
        for key in loot_item:
            setattr(item, key, loot_item[key])
        equip(item)
    else:
        loot()
        
    
def equip(item):
    plyr_cat = getattr(plyr, item.cat)
    if len(plyr_cat) == 2:
        swap(item)
    else:
        if item.cat == 'skills':
            if item.name in plyr.skills:
                swap(item)
            elif item.clss == "wiz" and plyr.clss == "Wizard":
                plyr_cat.append(item)
            elif item.clss == "war" and plyr.clss == "Warrior":
                plyr_cat.append(item)
            else: 
                print("\n" + "Wrong class")
        elif item.cat == 'equipment':
            setattr(plyr, item.typ, getattr(plyr, item.typ) + item.stat)
            plyr_cat.append(item)
        elif item.cat == 'inventory':
            plyr_cat.append(item)
        
    show_stats(plyr)
    loot()
    
    
    
def use(item):
    plyr_cat = getattr(plyr, item.cat)
    setattr(plyr, item.typ, getattr(plyr, item.typ) - item.stat)
    plyr_cat.remove(item)
    

def swap(item):
    print("\n" + "Only two items can fit in this slot.")
    plyr_cat = getattr(plyr, item.cat)
    plyr_cat_copy = plyr_cat.copy()
    for e in plyr_cat_copy:
        to_swap = input("Enter (1) to swap out " + e.name + ", Enter (P) to pass:")
        if to_swap == '1':
            if item.cat == 'equipment':
                use(e)
            else:
                plyr_cat.remove(e)
            equip(item)
            break
    print("\n" + "No items left")              
    

    
def battle(enemy):
    print("Enemy encountered!")
    
    #show enemy stats
     

    
         
def roll(die):
    return randint(1, die)
   
             

###STORY###
def story():
    loot()
    #battle()
    
    
newGame()

    

    
            