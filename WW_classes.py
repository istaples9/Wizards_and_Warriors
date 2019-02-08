# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:28:44 2019

@author: owner
"""
classes = {1: "Wizard", 2: "Warrior"}


class Char:
    
    def __init__(self, name, clss=None, lvl=0, exp=0, hp=0, mp=0, dmg=9, block=0, equipment=[], skills=[], inventory=[]):
        self.name = name
        self.clss = clss
        self.lvl = lvl
        self.exp = exp
        self.hp = hp
        self.mp = mp
        self.dmg = dmg
        self.block = block
        self.equipment = equipment
        self.skills = skills
        self.inventory = inventory
    
        
class Wizard(Char):
    
    def __init__(self, Char):
        super().__init__(self, hp=15, mp=15)
    
        
                 
class Warrior(Char):
    
    def __init__(self, Char):
        super().__init__(self, hp=15, mp=15)
       
         
        
class Goblin(Char):
    
    def __init__(self, Char):
        super().__init__(self, clss='Goblin', hp=7, mp=3, dmg=1.5, block=1, exp=1)

        
    def club_bash(self, skill, plyr=None):
        self.skill = "Club Bash"
        self.skill_description = f"Deals 2 Damage."
        plyr.block -= 2
        if plyr.block < 0:
            plyr.hp += plyr.block
            plyr.block = 0
    
    def battle_stance(self, skill, plyr=None):
        self.skill = "Battle Stance"
        self.skill_description = "Increases block by 2."
        self.block += 2
        
    
    enemy_skills = ['club_bash', 'battle_stance']
        



        