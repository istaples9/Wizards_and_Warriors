# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:28:44 2019

@author: owner
"""

classes = {1: "Wizard", 2: "Warrior"}

class Player:
    def __init__(self, name, hp=5, mp=5, dmg=0, block=0, equipment=[], skills=[], inventory=[]):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.dmg = dmg
        self.block = block
        self.equipment = equipment
        self.skills = skills
        self.inventory = inventory
    
    def __repr__(self, inventory):
        return f"{self.inventory}"
        
        
class Wizard(Player):
    
    def FireBall(self):
        print("Sears enemy for: " + str(self.dmg) + " dmg")
        
    def FrostBite(self):
        print("Freezes enemy for: " + str(self.dmg) + " turns.")
        
              
class Warrior(Player):
         
    def HeavyBlow(self):
        print("Bashes enemy for: " + str(self.dmg) + " dmg")
        
    def Fortify(self):
        print("Increases block by: 1")
        self.block += 1
    
                    

        



        