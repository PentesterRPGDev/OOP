"""
Loads everything beloging to the player
"""

import random
import time

class Player:
    """ creates a player class """
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
        hit = player.atk_lvl * (random.randint(1, 100)) * player.str_lvl
        slow_print(print(f"\n{player.name} deals {hit} damage."))
        return hit

    @classmethod
    def leveling(cls, player):
        pass

adventurer = Player(input("\nWhat's your name, dear adventurer? \n\n"))
print(adventurer)
hitting = Player.damage(adventurer)

def slow_print(text, delay=0.05):
    """ prints text slow, simulate reading """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# Display the question slowly
slow_print("What's your name, dear adventurer?", delay=0.2)
