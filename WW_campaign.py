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
import tkinter

#window = tkinter.Tk()
#window.title("Wizards and Warriors")
#window.mainloop()

def newGame():
    #Initiates player object and selects class.
    global plyr
    plyr_class = ""
    while plyr_class not in ['1', '2']:
        plyr_class = input("Choose class, enter(1) for Wizard and (2) for Warrior:")
    #Names player.
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
    #Prints player and enemy stats
    #clear()
    if char.clss not in WW_classes.classes.values():
        print("\n", char.clss, "|", "HP:", round(char.hp, 1), "|", "Block:", round(char.block, 1))
    else:
        print("\n", char.name, "|", char.clss, "|", "Lvl:", int(char.lvl), "|", "HP:", round(char.hp, 1), "|", "MP:", round(char.mp, 1), "|", "Dmg:", round(char.dmg, 1), "|", "Block:", round(char.block, 1), "|", "Accuracy:", round(char.acc, 1))
        cats = ['skills', 'equipment', 'inventory']
        for cat in cats:
            items = []
            char_cat = getattr(char, cat)
            for item in char_cat:
                if cat == 'skills':
                    cool_down_count = item.cool_down
                    if hasattr(item.cd, 'elapsed_turns'):
                        cool_down_count = item.cd.elapsed_turns
                    items.append([f" {item.name}, {item.typ}:{round(item.stat, 2)}, Mana Cost:{round(item.mana_cost, 2)}, Cool Down:{cool_down_count}/{item.cool_down}"])
                else: 
                    items.append([f" {item.name}, {item.typ}:{round(item.stat, 2)}"])
            print(f"{cat.capitalize()}: {items}")
        
        
def loot():
    #Selects random item from item list, calls equip function if player chooses Y.
    loot_item = np.random.choice(WW_items.items)
    WW_items.item_info(loot_item)
    pick_up = ""
    while pick_up.upper() not in ['Y', 'C']:
        pick_up = input(f"Enter (Y) to equip {loot_item['name']}, or (C) to cancel:")
    if pick_up.upper() == 'Y':
        equip(loot_item)
    elif pick_up.upper() == 'C':
        pass

    
def equip(item_skill):
    #If item / skill passed in is not already an instance of WW_items, initiates it.
    if not isinstance(item_skill, WW_items.Item):
        item = WW_items.Item(item_skill)
        for key in item_skill:
            setattr(item, key, item_skill[key])
    else:
        item = item_skill
    #checks if pack slot is full, if it is, swap function is called.
    plyr_cat = getattr(plyr, item.cat)
    if len(plyr_cat) == 2:
        print("\n", "Only two items can fit in this slot.")
        swap(item)
    elif item in plyr.skills:
        print("Only one of each skill allowed.")
        swap(item)
    #ads item / skill to player
    else:
        if item.cat == 'skills':
            plyr_cat.append(item)
        elif item.cat == 'equipment':
            if item.clss == plyr.clss:
                print("10% bonus for matching equipment class.")
                item.stat *= 1.10
            setattr(plyr, item.typ, getattr(plyr, item.typ) + item.stat)
            plyr_cat.append(item)
        elif item.cat == 'inventory':
            plyr_cat.append(item) 
        #Initiates cool down class for item.
        item.cd(item.cool_down)
    show_stats(plyr)

       
def choose():
    #If no item / skill is passed in, player selects one from pack.
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
        turn.turn -=1
        return
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
            turn.turn -=1
            return
        else:
            item = use_cat[int(use_index)-1]
            return item
 
def use(item, enemy=None):
    #after item has been selected or passed in, enemy and player stats are adjusted based on item stats and pack category.
    if item.cd.is_active(turn.turn) == False:
        if item.cat != 'equipment':
            if item.mana_cost <= plyr.mp:
                if item.cat == 'inventory':
                    drop(item)
                if item.typ == 'stun':
                    print("\n" + f"Enemy stunned for {item.stat} turn!")
                    turn.turn += 1
                elif item.typ == 'dmg':
                    print("\n" + f"Strikes enemy for {item.stat} damage!")
                    enemy.block -= item.stat
                    if enemy.block < 0:
                        enemy.hp += enemy.block
                        enemy.block = 0
                    else:
                        setattr(plyr, item.typ, getattr(plyr, item.typ) + item.stat)
                    plyr.mp -= item.mana_cost
                    item.cd.triggered_turn = turn.turn
                else:
                    print("\n" + "Not enough mana!")
                    use(None)
        else:
            print("\n" + f"Item on cool down: {item.cool_down-item.cd.elapsed_turns} turns left!")
            use(None, enemy)

def drop(item):
    #Drops item, if item category is equipment, player stats are adjusted.
    if item.cat == 'equipment':
        setattr(plyr, item.typ, getattr(plyr, item.typ) - item.stat)
    plyr_cat = getattr(plyr, item.cat)
    plyr_cat.remove(item)
    

def swap(item):
    #Swaps item if pack slots are full. Finds pack category for item.
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
    #Drops old item and equips new item.
    else:
        swap_item = plyr_cat[int(swap_index)-1]
        drop(swap_item)
        equip(item)
    
       
def battle(enemy):
    #Starts battle with passed in enemy, initiates turn object and randomly selects first move.
    global turn
    turn = Turn()
    turn.turn = roll(1)
    print("\n", f"{enemy.clss} encountered!")
    show_stats(enemy)
    while enemy.hp > 0 and plyr.hp > 0:
        #If turn is even, player goes, else, enemy.
        print(f"Turn:{turn.turn}")
        if turn.turn % 2 == 0:
            print("\n" + "Your turn:")
            move = ""
            inputs = ['1', '2']
            while move not in inputs:
                move = input("\n" + "Enter (1) to use physical attack, enter (2) to use item/skill:")
            if move == '1':
                print("\n" + f"You hit enemy for {round(plyr.dmg, 2)} damage!")
                enemy.block -= plyr.dmg
                if enemy.block < 0:
                    enemy.hp += enemy.block
                    enemy.block = 0
            #If player chooses to use item / skill, the use function is called.
            else:
                use(choose(), enemy)
        else:
            #Enemy uses a random skill from it's class.
            print("\n" + "Enemy turn...")
            time.sleep(1)
            rand_skill = random.choice(enemy.enemy_skills)
            skill = getattr(enemy, rand_skill)
            skill(rand_skill, plyr)
            print(f"{enemy.clss} used {enemy.skill}!" + "\n" + f"{enemy.skill_description}")
            show_stats(plyr)
        turn.turn += 1
    #If player wins, calls the loot function, adds block back to stats, and checks if player has leveled up.
    if enemy.hp <= 0:
        print("\n" + f"{enemy.clss} destroyed! You won an item: ")
        loot()
        block_items = [item.stat for item in plyr.equipment if item.typ=='block']
        plyr.block = sum(block_items)
        level_up(enemy)
    else:
        print("\n" + "You lose! game over.")


def level_up(enemy):
    #Levels up player if the enemy exp increases player level to a higher int.
    last_lvl = plyr.lvl
    new_lvl = plyr.lvl + enemy.exp
    int_diff = int(new_lvl) - int(last_lvl)
    #Levels up player for each higher int achieved and calls add skill function.
    for i in range(int_diff):
        print("\n" + "You leveled up!")
        plyr.lvl += enemy.exp/int_diff
        plyr.hp *= 1.1
        plyr.mp *= 1.1
        plyr.dmg *= 1.1
        plyr.block *= 1.1
        add_skill()


def add_skill():
    #Checks if there are any unlearned skills for the player that match player level and class.
    clss_skills = []
    if plyr.clss == "Wizard":
        clss_skills = WW_items.wizard_skills
    if plyr.clss == "Warrior":
        clss_skills = WW_items.warrior_skills
    for skill in clss_skills:
        skill_names = [skill.name for skill in plyr.skills]
        if skill['name'] not in skill_names:
            if int(plyr.lvl) >= skill['lvl']:
                print(f"You learned {skill['name']}!")
                equip(skill)
                
                       
class Turn: 
    def __init__(self, turn = 0):
        self.turn = turn

         
def roll(die):
    return randint(0 , 1)
   
def clear():
    os.system( 'cls' )
             

def story():
    loot()
    loot() 
    loot()
    battle(WW_classes.Goblin('Goblin'))
    battle(WW_classes.Goblin('Goblin'))
    
    
newGame()

    

    
            