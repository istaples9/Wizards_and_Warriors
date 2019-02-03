# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:11:32 2019

@author: owner
"""
import WW_classes
import WW_items
from random import randint
import numpy as np
import time
import os
import random

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
    #clear()
    if char.clss not in WW_classes.classes.values():
        print("\n", char.clss, "|", "HP:", char.hp, "|", "Block:", char.block)
    else:
        print("\n", char.name, "|", char.clss, "|", "Lvl:", char.lvl, "|", "HP:", char.hp, "|", "MP:", char.mp, "|", "Dmg:", char.dmg, "|", "Block:", char.block)
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
    
       
def use(item, enemy=None):
    if item == None:
        pack = [cat for cat in ["skills", "inventory"] if len(getattr(plyr, cat)) > 0]
        choose_cat = ""
        for i in range(len(pack)):
            cat = pack[i]
            choose_cat += (f"Enter ({i+1}) to use {cat.capitalize()}, ")
        inputs = [str(i) for i in range(1, len(pack)+1)]
        inputs += ["c", "C"]
        use_index = ""
        while use_index not in inputs:
            use_index = input(choose_cat + "or (C) to cancel: ")
        if use_index.upper() == "C":
            turn.turn += 1
        else:
            use_cat = getattr(plyr, pack[int(use_index)-1])
            choose_item = ""
            for i in range(len(use_cat)):
                choose_item += (f"Enter ({i+1}) to use {getattr(use_cat[i], 'name')}, ")
            inputs = [str(i) for i in range(1, len(use_cat)+1)]
            inputs += ["c", "C"]
            use_index = ""
            while use_index not in inputs:
                use_index = input(choose_item + "or (C) to cancel: ")
            if use_index.upper() == "C":
                pass
            else:
                item = use_cat[int(use_index)-1]
                use(item, enemy)
    else:
        if item.cat != 'equipment':
            if item.typ == 'stun':
                print("\n" + f"Enemy stunned for {item.stat} turn!")
                turn.turn += 1
            elif item.typ == 'dmg':
                print(f"strikes enemy for {item.stat} damage!")
                enemy.block -= item.stat
                if enemy.block < 0:
                    enemy.hp += enemy.block
                    enemy.block = 0
            else:
                setattr(plyr, item.typ, getattr(plyr, item.typ) + item.stat)
        drop(item)


def drop(item):
    if item.cat == 'equipment':
        setattr(plyr, item.typ, getattr(plyr, item.typ) - item.stat)
    plyr_cat = getattr(plyr, item.cat)
    plyr_cat.remove(item)
    

def swap(item):
    plyr_cat = getattr(plyr, item.cat)
    swap_num = ""
    for i in range(len(plyr_cat)):
        cat_item = getattr(plyr_cat[i], 'name')
        swap_num += (f"Enter ({i+1}) to swap for ({cat_item}), ")
    inputs = [str(i) for i in range(1, len(plyr_cat)+1)]
    inputs += ["c", "C"]
    swap_index = ""
    while swap_index not in inputs:
        swap_index = input(swap_num + "(C) to cancel: ")
    if swap_index.upper() == "C":
        pass
    else:
        swap_item = plyr_cat[int(swap_index)-1]
        if item.cat == 'equipment':
            drop(swap_item)
        else:
            plyr_cat.remove(swap_item)
        equip(item)
    
       
def battle(enemy):
    global turn
    print("\n", f"{enemy.clss} encountered!")
    show_stats(enemy)
    turn = Turn()
    turn.turn = roll(1)
    while enemy.hp > 0 and plyr.hp > 0:
        show_stats(plyr)
        show_stats(enemy)
        if turn.turn % 2 == 0:
            print("\n" + "Your turn:")
            move = ""
            inputs = ['1', '2']
            while move not in inputs:
                move = input("\n" + "Enter (1) to use physical attack, enter (2) to use item/skill:")
            if move == '1':
                print("\n" + f"You hit enemy for {plyr.dmg} damage!")
                enemy.block -= plyr.dmg
                if enemy.block < 0:
                    enemy.hp += enemy.block
                    enemy.block = 0
            else:
                use(None, enemy)
            turn.turn += 1
        else:
            print("\n" + "Enemy turn...")
            time.sleep(1)
            rand_skill = random.choice(enemy.enemy_skills)
            skill = getattr(enemy, rand_skill)
            skill(rand_skill, plyr)
            print(f"{enemy.clss} used {enemy.skill}!" + "\n" + f"{enemy.skill_description}")
            turn.turn += 1
    else:
        if enemy.hp <= 0:
            print("\n" + f"{enemy.clss} destroyed! You won an item: ")
            level_up(enemy)
            loot()
        else:
            print("\n" + "You lose! game over.")

def level_up(enemy):
    before_exp = plyr.exp
    plyr.exp += enemy.exp
    if int(plyr.exp) > int(before_exp):
        print("You leveled up!")
                   
class Turn: 
    def __init__(self, turn = 0):
        self.turn = turn

         
def roll(die):
    return randint(0 , die+1)
   
def clear():
    os.system( 'cls' )
             

def story():
    loot()
    loot() 
    loot()
    battle(WW_classes.Goblin('Goblin'))
    
    
newGame()

    

    
            