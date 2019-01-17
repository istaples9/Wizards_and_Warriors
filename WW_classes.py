# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:28:44 2019

@author: owner
"""

classes = {1: "Wizard", 2: "Warrior"}

class Player:
    def __init__(self, name, hp=5, mp=5, dmg=0, block=0, inventory=[], skills=[]):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.dmg = dmg
        self.block = block
        self.inventory = inventory
        self.skills = skills
    
    def __repr__(self, inventory):
        return f"{self.inventory}"
        
        
class Wizard(Player):
    
    def fireBall(self):
        print("Sears enemy for: " + str(self.dmg) + " dmg")
        
    def frostBite(self):
        print("Freezes enemy for: " + str(self.dmg) + " turns.")
        
              
class Warrior(Player):
         
    def heavyBlow(self):
        print("Bashes enemy for: " + str(self.dmg) + " dmg")
        
    def fortify(self):
        print("Increases block by: 1")
        self.block += 1
    
                    

        



        