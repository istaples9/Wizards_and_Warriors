# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:05:14 2019

@author: owner
"""

hammer = {'name': 'Hammer',
          'clss': 'Warrior',
          'description': 'Rusty blacksmith hammer',
          'typ': 'dmg',
          'stat': 3,
          'cat': 'equipment'
         }

wooden_shield = {'name': 'Wooden Shield',
                 'clss': 'Warrior',
                 'description': 'Old and rotted shield',
                 'typ': 'block',
                 'stat': 2,
                 'cat': 'equipment'
                }

helmet = {'name': 'Helmet',
          'clss': 'Warrior',
          'description': 'Dented helmet',
          'typ': 'block',
          'stat': 1,
          'cat': 'equipment'
         }

cape = {'name': 'Cape',
        'clss': 'Wizard',
        'description': 'Magical tattered cape',
        'typ': 'mp',
        'stat': 2,
        'cat': 'equipment'
       }

staff = {'name': 'Staff',
         'clss': 'Wizard',
         'description': 'Long, ergonomic stick',
         'typ': 'dmg',
         'stat': 2,
         'cat': 'equipment'
        }

wand = {'name': 'Wand',
        'clss': 'Wizard',
        'description': 'Long, ergonomic stick',
        'typ': 'dmg',
        'stat': 1,
        'cat': 'equipment'
       }

minor_mana_potion = {'name': 'Minor Mana Potion',
                     'clss': None,
                     'description': 'Increases player mana on use.',
                     'typ': 'mp',
                     'stat': 1,
                     'cat': 'inventory'
                    }

minor_health_potion = {'name': 'Minor Health Potion',
                       'clss': None,
                       'description': 'Increases player health on use.',
                       'typ': 'hp',
                       'stat': 1,
                       'cat': 'inventory'
                      }

heavy_blow = {'name': 'Heavy Blow',
              'clss': 'Warrior',
              'description': 'Smashes enemies',
              'typ': 'dmg',
              'stat': 3,
              'mana_cost': 1,
              'cool_down': 1,
              'cat': 'skills'
             }

fortify = {'name': 'Heavy Blow',
              'clss': 'Warrior',
              'description': 'Smashes enemies',
              'typ': 'block',
              'stat': 3,
              'mana_cost': 1,
              'cool_down': 1,
              'cat': 'skills'
             }

frost_bite = {'name': 'Frost Bite',
              'clss': 'Wizard',
              'description': 'Freezes enemies',
              'typ': 'stun',
              'stat': 1,
              'mana_cost': 3,
              'cool_down': 1,
              'cat': 'skills'
             }

ice_shell = {'name': 'Ice Shell',
              'clss': 'Wizard',
              'description': 'Casts a frosty armor around yourself',
              'typ': 'block',
              'stat': 3,
              'mana_cost': 3,
              'cool_down': 1,
              'cat': 'skills'
             }

items = [hammer, wooden_shield, helmet, cape, staff, wand, minor_mana_potion, minor_health_potion, heavy_blow, fortify, frost_bite, ice_shell]


def item_info(item):
    print("\n")
    print(f"{item['name']}, Class:{item['clss']}, {item['typ']}:{item['stat']}")
    print(f"Description: {item['description']}")
    
    


class Item:
    
    def __init__(self, name=None, clss=None, description=None, typ=None, stat=None, mana_cost=None, cool_down=None, cat=None):
        self.name = name
        self.clss = clss
        self.description = description
        self.typ = typ
        self.stat = stat
        self.mana_cost = mana_cost
        self.cool_down = cool_down
        self.cat = cat
        
    


    
