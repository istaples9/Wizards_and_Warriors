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

rogues_ring = {'name': 'Rogues Ring',
               'clss': None,
               'description': 'Inceases accuracy',
               'typ': 'acc',
               'stat': 2,
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
                     'stat': 3,
                     'cat': 'inventory'
                    }

minor_health_potion = {'name': 'Minor Health Potion',
                       'clss': None,
                       'description': 'Increases player health on use.',
                       'typ': 'hp',
                       'stat': 3,
                       'cat': 'inventory'
                      }

dexterity_potion = {'name': 'Minor Health Potion',
                    'clss': None,
                    'description': 'Increases player accuracy on use.',
                    'typ': 'acc',
                    'stat': 3,
                    'cat': 'inventory'
                   }

items = [hammer, wooden_shield, helmet, rogues_ring, cape, staff, wand, minor_mana_potion, minor_health_potion, dexterity_potion]


frost_bite = {'name': 'Frost Bite',
              'clss': 'Wizard',
              'lvl': 1,
              'description': 'Freezes enemies',
              'typ': 'stun',
              'stat': 1,
              'mana_cost': 2,
              'cool_down': 4,
              'cat': 'skills'
             }

ice_shell = {'name': 'Ice Shell',
             'clss': 'Wizard',
             'lvl': 2,
             'description': 'Casts a frosty armor around yourself',
             'typ': 'block',
             'stat': 4,
             'mana_cost': 2,
             'cool_down': 4,
             'cat': 'skills'
            }

wizards_focus = {'name': 'Wizards Focus',
                 'clss': 'Wizard',
                 'lvl': 2,
                 'description': 'Enters a state of intense concentration',
                 'typ': 'acc',
                 'stat': 3,
                 'mana_cost': 2,
                 'cool_down': 4,
                 'cat': 'skills'
                 }

heavy_blow = {'name': 'Heavy Blow',
              'clss': 'Warrior',
              'lvl': 1,
              'description': 'Smashes enemies',
              'typ': 'dmg',
              'stat': 3,
              'mana_cost': 2,
              'cool_down': 4,
              'cat': 'skills'
             }

fortify = {'name': 'Fortify',
           'clss': 'Warrior',
           'lvl': 2,
           'description': 'Increases block',
           'typ': 'block',
           'stat': 4,
           'mana_cost': 2,
           'cool_down': 4,
           'cat': 'skills'
          }

battle_zen = {'name': 'Battle Zen',
              'clss': 'Warrior',
              'lvl': 2,
              'description': 'Hones in focus.',
              'typ': 'acc',
              'stat': 3,
              'mana_cost': 2,
              'cool_down': 4,
              'cat': 'skills'
             }

wizard_skills = [frost_bite, ice_shell, wizards_focus]

warrior_skills = [heavy_blow, fortify, battle_zen]



def item_info(item):
    print("\n")
    print(f"{item['name']}, Class:{item['clss']}, {item['typ']}:{item['stat']}")
    print(f"Description: {item['description']}")
    
class coolDown:
    
    def __init__(self, cool_down, triggered_turn=0):
        self.cool_down = cool_down
        self.triggered_turn = triggered_turn
         
    def is_active(self, current_turn):
        self.current_turn = current_turn
        self.elapsed_turns = self.current_turn - self.triggered_turn
        if self.elapsed_turns == self.current_turn:
            return False
        elif self.elapsed_turns == self.cool_down:
            return False
        else:
            return True

class Item(coolDown):
    
    def __init__(self, name=None, clss=None, description=None, typ=None, stat=0, acc=0, mana_cost=0, cool_down=0, cat=None):
        self.name = name
        self.clss = clss
        self.description = description
        self.typ = typ
        self.stat = stat
        self.mana_cost = mana_cost
        self.acc = acc
        self.cool_down = cool_down
        self.cat = cat
        
    def cd(self, cool_down):
        self.cd = coolDown(cool_down)

        
        
        
        

    


    
