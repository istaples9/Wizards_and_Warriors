# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:05:14 2019

@author: owner
"""
import WW_classes

atk_itms = {0: "Hammer", 1: "Staff"}
def_itms = {2: "Wooden Shield", 3: "Wizards Hat"}
hp_itms = {4: "Apple Pie", 5: "Snickers Bar"}
items = atk_itms.copy()
items.update(def_itms)
items.update(hp_itms)

class Stats:
    
    def __init__(self, item, stats=1):
        self.item = item
        self.stats = stats
        
    


    
