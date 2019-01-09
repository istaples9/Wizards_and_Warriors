# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:28:44 2019

@author: owner
"""

class Player:
    def __init__(self, name, dmg=0, block=0):
        self.name = name
        self.dmg = dmg
        self.block = block
              
class Warrior(Player):
    
    def heavyBlow(self):
        print("Bashes enemy for: " + str(self.dmg) + " dmg")
        
    def fortify(self):
        print("Increases block by: 1")
        self.block += 1
                    
class Wizard(Player):
    
    def fireBall(self):
        print("Sears enemy for: " + str(self.dmg) + " dmg")
        
    def frostBite(self):
        print("Freezes enemy for: " + str(self.dmg) + " dmg")
        
merlin = Wizard("merlin")


        