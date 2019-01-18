# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:05:14 2019

@author: owner
"""
import WW_classes

atk_itms = {1: "Hammer", 2: "Staff"}
def_itms = {3: "Wooden Shield", 4: "Helmet"}
hp_itms = {5: "Apple Pie", 6: "Snickers Bar"}
mp_itms = {7: "Minor Mana Potion", 8: "Mana Potion"}
wizard_tomes = {9: "FireBall", 10: "FrostBite"}
warrior_tomes = {11: "HeavyBlow", 12: "Fortify"}

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
        
    


    
