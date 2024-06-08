"""
Load the player skills, status and features.
"""

import random
import time
import os

class Player:
    """ create a player class """
    def __init__(self, name):
        self.name = name
        self.atk_lvl = 1
        self.str_lvl = 1
        self.lp_lvl = 300
        self.def_lvl = 1
        self.xp = 0

    def __str__(self):
        return f"\n{self.name} has {self.lp_lvl} live points."

    @classmethod
    def damage(cls, player):
        """ calculates player's damage """
        hit = player.atk_lvl * (random.randint(0, 100)) * player.str_lvl
        print(f"\n{player.name} deals {hit} damage.")
        return hit

    @classmethod
    def level_str(cls, player):
        """ create lvl in str """
        if player.xp <= 3:
            player.str_lvl += 1

class Monster:
    """ create a monster class """
    def __init__(self, name, atk_lvl, str_lvl, lp_lvl, def_lvl, xp):
        self.name = name
        self.atk_lvl = atk_lvl
        self.str_lvl = str_lvl
        self.lp_lvl = lp_lvl
        self.def_lvl = def_lvl
        self.xp = xp

    def __str__(self):
        return f"\n{self.name} has {self.lp_lvl} live points."

    @classmethod
    def damage(cls,monster):
        """ calculate monster damage """
        hit = monster.atk_lvl * (random.randint(0, 10)) * monster.str_lvl
        print(f"\n{monster.name} deals {hit} damage.")
        return hit

adventurer = Player(input("\nWhat's your name, dear adventurer? \n\n"))
print(adventurer)
goblin = Monster("goblin", 1, 1, 600, 1, 3)
print(goblin)

class Fight(Player, Monster):

    def __str__(self):
        return "Start the fight"

    def fighting(self):
        """ start the fight """
        while adventurer.lp_lvl > 0 and goblin.lp_lvl > 0:
            dmg = Player.damage
            goblin.lp_lvl -= dmg
            print(goblin.lp_lvl)

fight = Fight()
