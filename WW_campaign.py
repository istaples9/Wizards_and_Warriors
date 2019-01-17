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
    global name
    global hp
    global clss
    try:
        plyr_class = int(input("Choose class, enter(1) for Wizard and (2) for Warrior:"))
    except:
        print("Invalid class.")
        return newGame()
    if plyr_class not in WW_classes.classes:
        print("Invalid class.")
        return newGame()
    name = input("Name your character: ")
    clss = WW_classes.classes[plyr_class]
    if plyr_class == 1:
        name = WW_classes.Wizard(name)
    if plyr_class == 2:
        name = WW_classes.Warrior(name)
    hp = name.hp
    story()
    
    
def show_stats():
    print("\n", name.name, "|", clss, "|", "HP:", name.hp, "|", "MP:", name.mp, "|", "Dmg:", name.dmg, "|", "Block:", name.block)
    print("Skills: ", name.skills)
    print("Equipment: ", name.equipment)
    print("Inventory: ", name.inventory)
    
    
def loot():
    n = len(WW_items.items) - 1
    item = WW_items.items[roll(n)]
    item = WW_items.Stats(item, roll(tier[1]))
    if item.item in WW_items.atk_itms.values():
        print(item.item, "|", "Dmg:", item.stats)
        equip(item, "dmg")
    elif item.item in WW_items.def_itms.values():
        print(item.item, "|", "Block:", item.stats)
        equip(item, "block")
    elif item.item in WW_items.hp_itms.values():
        print(item.item, "|", "HP +", item.stats)
        equip(item, "hp")
    elif item.item in WW_items.mp_itms.values():
        print(item.item, "|", "MP +", item.stats)
        equip(item, "mp")
    elif item.item in WW_items.wizard_tomes.values():
        x = WW_classes.Wizard(name)
        print("Wizard Tome", "|",item.item, "|", "|", "Mana: ", item.mana)
        equip(item, "wiz")
    elif item.item in WW_items.warrior_tomes.values():
        x = WW_classes.Warrior(name)
        print("Warrior Tome", "|",item.item, "|", "|", "Mana: ", item.mana)
        equip(item, "war")
    
    
    
def equip(item, typ):
    pick_up = input("Equip?")
    if pick_up.lower() == "y":
        if typ == "dmg":
            name.dmg += item.stats
            name.equipment.append([item.item, "Dmg:" + str(item.stats)])
        if typ == "block":
            name.block += item.stats
            name.equipment.append([item.item, "Block:" + str(item.stats)])
        if typ == "hp":
            name.inventory.append([item.item, "HP+" + str(item.stats)])
        if typ == "mp":
            name.inventory.append([item.item, "MP+" + str(item.stats)])
        if typ == "wiz" and clss == "Wizard":
            name.skills.append([item.item, "blank"])
        if typ == "war" and clss == "Warrior":
            name.skills.append([item.item, "blank"])
        else:
            print("\n" + "wrong class")
    show_stats()
    
         
def roll(n):
    return randint(0, n)
   
             

###STORY###
def story():
    loot()
    
    
newGame()
    

    
            