# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:05:14 2019

@author: owner
"""

hammer = {'name': 'Hammer',
          'clss': 'war',
          'description': 'Rusty blacksmith hammer',
          'typ': 'dmg',
          'stat': 3,
          'mana_cost': 0,
          'cool_down': 1,
          'cat': 'equipment'
         }

wooden_shield = {'name': 'Wooden Shield',
                 'clss': 'war',
                 'description': 'Old and rotted shield',
                 'typ': 'block',
                 'stat': 2,
                 'mana_cost': 0,
                 'cool_down': 1,
                 'cat': 'equipment'
                }

helmet = {'name': 'Helmet',
          'clss': 'war',
          'description': 'Dented helmet',
          'typ': 'block',
          'stat': 1,
          'mana_cost': 0,
          'cool_down': 1,
          'cat': 'equipment'
         }

staff = {'name': 'Staff',
         'clss': 'wiz',
         'description': 'Long, ergonomic stick',
         'typ': 'dmg',
         'stat': 2,
         'mana_cost': 0,
         'cool_down': 1,
         'cat': 'equipment'
        }

wand = {'name': 'Wand',
        'clss': 'wiz',
        'description': 'Long, ergonomic stick',
        'typ': 'dmg',
        'stat': 1,
        'mana_cost': 0,
        'cool_down': 1,
        'cat': 'equipment'
       }

minor_mana_potion = {'name': 'Minor Mana Potion',
                     'clss': None,
                     'description': 'Increases player mana.',
                     'typ': 'mp',
                     'stat': 1,
                     'mana_cost': 0,
                     'cool_down': 0,
                     'cat': 'inventory'
                    }

minor_health_potion = {'name': 'Minor Health Potion',
                       'clss': None,
                       'description': 'Increases player health.',
                       'typ': 'hp',
                       'stat': 1,
                       'mana_cost': 0,
                       'cool_down': 0,
                       'cat': 'inventory'
                      }

heavy_blow = {'name': 'Heavy Blow',
              'clss': 'war',
              'description': 'Smashes enemies',
              'typ': 'dmg',
              'stat': 1,
              'mana_cost': 1,
              'cool_down': 1,
              'cat': 'skills'
             }

frost_bite = {'name': 'Frost Bite',
              'clss': 'wiz',
              'description': 'Freezes enemies',
              'typ': 'stun',
              'stat': 1,
              'mana_cost': 3,
              'cool_down': 1,
              'cat': 'skills'
             }

ice_shell = {'name': 'Ice Shell',
              'clss': 'wiz',
              'description': 'Casts a frosty armor around yourself',
              'typ': 'stun',
              'stat': 1,
              'mana_cost': 3,
              'cool_down': 1,
              'cat': 'skills'
             }

items = [hammer, wooden_shield, helmet, staff, wand, minor_mana_potion, minor_health_potion, heavy_blow, frost_bite]


def item_info(item):
    print("\n")
    print(f"{item['name']}, {item['typ']}:{item['stat']}, mana cost:{item['mana_cost']}, cool down:{item['cool_down']}")
    print(f"Description: {item['description']}")
    
    


class Item:
    
    def __init__(self, name=None, clss=None, description=None, typ=None, stat=None, mana_cost=None, cool_down=None, cat=None):
        self.name = name
        self.clss = clss
        self.description = description
        self.typ = typ
        self.stats = stat
        self.mana_cost = mana_cost
        self.cool_down = cool_down
        self.cat = cat
        
    


    
