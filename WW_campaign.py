# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:11:32 2019

@author: owner
"""
import WW_classes
import WW_items
from random import randint 


loot_ops = {0: "You found a tresure chest!"}

tier = {1: 4}


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
    plyr = input("Name your character: ")
    plyr_class = WW_classes.classes[plyr_class]
    if plyr_class == "Wizard":
        plyr = WW_classes.Wizard(plyr)
    if plyr_class == "Warrior":
        plyr = WW_classes.Warrior(plyr)
    plyr.clss = plyr_class
    story()
    
    
def show_stats(char):
    print("\n", char.name, "|", char.clss, "|", "HP:", char.hp, "|", "MP:", char.mp, "|", "Dmg:", char.dmg, "|", "Block:", char.block)
    print("Skills: ", char.skills)
    print("Equipment: ", char.equipment)
    print("Inventory: ", char.inventory)
    
    
def loot():
    global skill_type
    n = len(WW_items.items) - 1
    name = WW_items.items[roll(n)]
    item = WW_items.Item(name)
    item.name = name
    item.stats = roll(tier[1])
    if item.name in WW_items.atk_itms.values():
        item.typ = 'dmg'
        item.cat = 'equipment'
        print("\n", item.name, "|", "Dmg:", item.stats)
    elif item.name in WW_items.def_itms.values():
        item.typ = 'block'
        item.cat = 'equipment'
        print("\n", item.name, "|", "Block:", item.stats)
    elif item.name in WW_items.hp_itms.values():
        item.typ = 'hp'
        item.cat = 'inventory'
        print("\n", item.name, "|", "HP +", item.stats)
    elif item.name in WW_items.mp_itms.values():
        item.typ = 'mp'
        item.cat = 'inventory'
        print("\n", item.name, "|", "MP +", item.stats)
    elif item.name in WW_items.wizard_tomes.values():
        item.typ = 'wiz'
        item.cat = 'skills'
        skill_type = WW_classes.Wizard.attack(item.name)
        print("\n", "Wizard Tome", "|", item.name, "|", "Mana:", item.mana, "|", skill_type, item.stats)
    elif item.name in WW_items.warrior_tomes.values():
        item.typ = 'war'
        item.cat = 'skills'
        skill_type = WW_classes.Wizard.attack(item.name)
        print("\n", "Warrior Tome", "|", item.name, "|", "Mana:", item.mana, "|", skill_type, item.stats)
    choice = int(input("Enter (1) to equip item or enter nothing to cancel:"))
    if choice == 1:
        equip(item)
    
    
def equip(item):
    plyr_cat = getattr(plyr, item.cat)
    if item.name in plyr_cat:
        swap(item)
    elif len(plyr_cat) < 2 and item.name not in plyr_cat:
        if item.typ == "wiz" and plyr.clss == "Wizard":
            plyr_cat[item.name] = ["Mana:", item.mana, skill_type, item.stats]
        elif item.typ == "war" and plyr.clss == "Warrior":
            plyr_cat[item.name] = ["Mana:", item.mana, skill_type, item.stats]
        elif item.typ == 'dmg' or item.typ == 'block':
            setattr(plyr, item.typ, getattr(plyr, item.typ) + item.stats)
            plyr_cat[item.name] = [item.typ, item.stats]
        elif item.typ == 'hp' or item.typ == 'mp':
            plyr_cat[item.name] = [item.typ, item.stats]
        else: 
            print("\n" + "Wrong class")
    show_stats(plyr)
    
    
    
def use(item):
    if item.name in plyr.skills:
        plyr.skills.pop(item.name)
    elif item.name in plyr.equipment:
        setattr(plyr, item.typ, getattr(plyr, item.typ) - item.stats)
        plyr.equipment.pop(item.name)
    elif item.name in plyr.inventory:
        setattr(plyr, item.typ, getattr(plyr, item.typ) + item.stats)
        plyr.inventory.pop(item.name)
    else:  
        print("Not in pack")
    

def swap(item):
    plyr_cat = getattr(plyr, item.cat)
    cat_lst = list(plyr_cat)
    if item.name in plyr_cat:
        choice = int(input("You can only have on of each item in your inventory, enter (1) to swap " + str(item.name) + " or enter nothing to cancel:"))
        if choice == 1:
            plyr_cat.pop(item.name)
            equip(item)
        else:
            story()
    elif len(cat_lst) == 2 and item.name not in plyr_cat:
        choice = int(input("Choose item to drop, enter (1) for " + str(cat_lst[0]) + ", (2) for " + str(cat_lst[1]) + ", or enter nothing to cancel:"))
        if choice == 1:
            x = cat_lst[0]
            swap_item = WW_items.Item(x)
            swap_item.stats = plyr_cat[x][-1]
            swap_item.typ = plyr_cat[x][-2]
            use(swap_item)
            equip(item)
        elif choice == 2:
            x = cat_lst[1]
            swap_item = WW_items.Item(x)
            swap_item.stats = plyr_cat[x][-1]
            swap_item.typ = plyr_cat[x][-2]
            use(swap_item)
            equip(item)
    elif len(cat_lst) == 1 and item.name not in plyr_cat:
        choice = int(input("Choose item to drop, enter (1) for " + str(cat_lst[0]) + ", or enter nothing to cancel:"))
        if choice == 1:
            x = cat_lst[0]
            swap_item = WW_items.Item(x)
            swap_item.stats = plyr_cat[x][-1]
            swap_item.typ = plyr_cat[x][-2]
            use(swap_item)
            equip(item)
            
            
        
    
    
    
    
def battle(enemy):
    print("Enemy encountered!")
    
    #show enemy stats
     

    
         
def roll(n):
    return randint(1, n)
   
             

###STORY###
def story():
    loot()
    
    
newGame()

    

    
            