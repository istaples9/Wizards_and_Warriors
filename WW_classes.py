# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:28:44 2019

@author: owner
"""

classes = {1: "Wizard", 2: "Warrior"}

class Player:
    def __init__(self, name, clss=None, hp=5, mp=5, dmg=0, block=0, equipment={}, skills={}, inventory={}):
        self.name = name
        self.clss = clss
        self.hp = hp
        self.mp = mp
        self.dmg = dmg
        self.block = block
        self.equipment = equipment
        self.skills = skills
        self.inventory = inventory
    
        
class Wizard(Player):
    
    
    def attack(skill):
        description = ""
        if str(skill) == 'FireBall':
            description = "Burn Dmg:"
            return description
        if str(skill) == 'FrostBite':
            description = "Freeze:"
            return description
    
                 
class Warrior(Player):
         
    def attack(skill):
        if str(skill) == 'HeavyBlow':
            description = "Stun: "
            return description
        if str(skill) == 'Fortify':
            description = "Block+"
            return description
        
class Enemy(Player):
    
    print("enemy")
        



        