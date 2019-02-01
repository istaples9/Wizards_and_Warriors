# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:28:44 2019

@author: owner
"""

classes = {1: "Wizard", 2: "Warrior"}
pack_slots = ["skills", "equipment", "inventory"]

class Char:
    
    def __init__(self, name, clss=None, hp=0, mp=0, dmg=2, block=0, equipment=[], skills=[], inventory=[]):
        self.name = name
        self.clss = clss
        self.hp = hp
        self.mp = mp
        self.dmg = dmg
        self.block = block
        self.equipment = equipment
        self.skills = skills
        self.inventory = inventory
    
        
class Wizard(Char):
    
    def __init__(self, Char):
        super().__init__(self, hp=5, mp=10)
    
        
                 
class Warrior(Char):
    
    def __init__(self, Char):
        super().__init__(self, hp=10, mp=5)
       
         
        
class Goblin(Char):
    
    def __init__(self, Char):
        super().__init__(self, clss='Goblin', hp=7, mp=3, dmg=2, block=1)
        



        