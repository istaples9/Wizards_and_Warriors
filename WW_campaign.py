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
    item = WW_items.Stats(name)
    item.name = name
    item.stats = roll(tier[1])
    if item.name in WW_items.atk_itms.values():
        item.typ = 'dmg'
        print("\n", item.name, "|", "Dmg:", item.stats)
    elif item.name in WW_items.def_itms.values():
        item.typ = 'block'
        print("\n", item.name, "|", "Block:", item.stats)
    elif item.name in WW_items.hp_itms.values():
        item.typ = 'hp'
        print("\n", item.name, "|", "HP +", item.stats)
    elif item.name in WW_items.mp_itms.values():
        item.typ = 'mp'
        print("\n", item.name, "|", "MP +", item.stats)
    elif item.name in WW_items.wizard_tomes.values():
        item.typ = 'wiz'
        skill_type = WW_classes.Wizard.attack(item)
        print("\n", "Wizard Tome", "|", item.name, "|", "Mana:", item.mana, "|", skill_type, item.stats)
    elif item.name in WW_items.warrior_tomes.values():
        item.typ = 'war'
        skill_type = WW_classes.Wizard.attack(item)
        print("\n", "Warrior Tome", "|", item.name, "|", "Mana:", item.mana, "|", skill_type, item.stats)
    equip(item)
    
    
    
def equip(item):
    pick_up = input("Equip?")
    if pick_up.lower() == "y":
        if item.typ == "dmg":
            plyr.dmg += item.stats
            plyr.equipment[item.name] = ["Dmg:", item.stats]
        elif item.typ == "block":
            plyr.block += item.stats
            plyr.equipment[item.name] = ["Block:", item.stats]
        elif item.typ == "hp":
            plyr.inventory[item.name] = ["HP+", item.stats]
        elif item.typ == "mp":
            plyr.inventory[item.name] = ["MP+", item.stats]
        elif item.typ == "wiz" and plyr.clss == "Wizard":
            plyr.skills[item.name] = ["Mana:", item.mana, skill_type, item.stats]
        elif item.typ == "war" and plyr.clss == "Warrior":
            plyr.skills[item.name] = ["Mana:", item.mana, skill_type, item.stats]
        else:
            print("\n" + "wrong class")
    show_stats(plyr)
    use(item)
    
    
    
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
    show_stats(plyr)
    
    
    
    
def battle(enemy):
    print("Enemy encountered!")
    
    #show enemy stats
     

    
         
def roll(n):
    return randint(1, n)
   
             

###STORY###
def story():
    loot()
    
    
newGame()

    

    
            