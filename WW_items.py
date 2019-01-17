# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:05:14 2019

@author: owner
"""
import WW_classes

atk_itms = {0: "Hammer", 1: "Staff"}
def_itms = {2: "Wooden Shield", 3: "Wizards Hat"}
hp_itms = {4: "Apple Pie", 5: "Snickers Bar"}
mp_itms = {6: "Minor Mana Potion", 7: "Mana Potion"}
wizard_tomes = {8: "FireBall", 9: "FrostBite"}
warrior_tomes = {10: "HeavyBlow", 11: "Fortify"}

items = atk_itms.copy()
items.update(def_itms)
items.update(hp_itms)
items.update(mp_itms)
items.update(wizard_tomes)
items.update(warrior_tomes)

class Stats:
    
    def __init__(self, item, stats=1, mana=1):
        self.item = item
        self.stats = stats
        self.mana = mana
        
    


    
