import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.atk = 1
        self.dmg = 1
        self.hp = 300
        self.shield = 1
        self.xp = 2
    
    @classmethod
    def damage(cls, player):
        hit = player.atk * (random.randint(1, 10)) * player.dmg
        return hit

player1 = Player("Test")

hitting = Player.damage(player1)
print(f"deals {hitting}")
