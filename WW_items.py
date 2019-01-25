# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:05:14 2019

@author: owner
"""

atk_itms = {1: "Hammer", 2: "Staff", 3: "Wand"}
def_itms = {4: "Wooden Shield", 5: "Helmet", 6: "Cape"}
hp_itms = {7: "Apple Pie", 8: "Snickers Bar", 9: "Health Potion"}
mp_itms = {10: "Minor Mana Potion", 11: "Mana Potion", 12: "Witches Brew"}
wizard_tomes = {13: "FireBall", 14: "FrostBite"}
warrior_tomes = {15: "HeavyBlow", 16: "Fortify"}

items = atk_itms.copy()
items.update(def_itms)
items.update(hp_itms)
items.update(mp_itms)
items.update(wizard_tomes)
items.update(warrior_tomes)

class Item:
    
    def __init__(self, name, typ=None, cat=None, stats=1, mana=1):
        self.name = name
        self.typ = typ
        self.cat = cat
        self.stats = stats
        self.mana = mana
        
    


    
