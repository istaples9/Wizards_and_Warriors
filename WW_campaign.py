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
    show_stats(plyr)
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
        print("\n", "Only two items can fit in this slot.")
        swap(item)
    elif item in plyr.skills:
        print("Only one of each skill allowed.")
        swap(item)
    else:
        if item.cat == 'skills':
            if item.clss == plyr.clss:
                plyr_cat.append(item)
            else: 
                print("\n" + "Wrong class")
        elif item.cat == 'equipment':
            if item.clss == plyr.clss:
                print("25% bonus for matching equipment class.")
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
    plyr_cat = getattr(plyr, item.cat)
    swap_num = ""
    for i in range(len(plyr_cat)):
        cat_item = getattr(plyr_cat[i], 'name')
        swap_num += (f"Enter ({i+1}) to swap for ({cat_item}), ")
    inputs = [str(i) for i in range(1, len(plyr_cat)+1)]
    swap_index = ""
    while swap_index not in inputs:
        swap_index = input(swap_num)
    swap_item = plyr_cat[int(swap_index)-1]
    if item.cat == 'equipment':
        use(swap_item)
    else:
        plyr_cat.remove(swap_item)
    equip(item)
    
    
    
def battle(enemy):
    print("\n", "Enemy encountered!")
    show_stats(enemy)
    turn = roll(2)
    action = ""
    if turn == 1:
        while action not in ['1', '2', '3']:
            action = input("\n" + "Your turn! Enter (1) to use a skill, (2) to use a physical attack, or (3) to use an item: ")
        if action == '1' and len(plyr.skills) > 0:
            print(f"Enter (1) for {plyr.skills[0]}")
        elif action == '2':
            print("attack")
        elif action == '3' and len(plyr.inventory) > 0:
            print(plyr.inventory)
        else:
            print("Attacking is your only option:")
    else:
        print("\n", "Enemy turn:")
     
 
    
         
def roll(die):
    return randint(1, die+1)
   
             

###STORY###
def story():
    loot()
    battle(WW_classes.Goblin('Goblin'))
    
    
newGame()

    

    
            