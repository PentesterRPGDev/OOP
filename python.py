class Monster:
    def __init__(self, name, hp, atk, dmg, exp):
        self.name = name
        self.health = hp
        self.attack = atk
        self.damage = dmg
        self.exp = exp

    def __str__(self):
        return f"{self.name} has {self.health} hp."

class Player:
    def __init__(self, name, hp, atk, dmg):
        self.name = name
        self.health = hp
        self.attack = atk
        self.damage = dmg
        self.exp = 0

    def __str__(self):
        return f"{self.name} has {self.health} hp."

class Fight:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start_fight(self):
        while self.player.health > 0 and self.monster.health > 0:
            self.monster.health -= self.player.attack * self.player.damage
            print(f"You attack the {self.monster.name} and deal {self.player.attack * self.player.damage} damage.")
        if self.monster.health > 0:
            print(f"{self.monster.name}'s turn:")
            self.player.health -= self.monster.attack * self.monster.damage
            print(f"The {self.monster.name} attacks you and deals {self.monster.attack * self.monster.damage} damage.")
        if self.player.health <= 0:
            print(f"You have been defeated by the {self.monster.name}.")
        else:
            print(f"You have defeated the {self.monster.name}!")
            print(f"You gained {self.monster.exp} experience points.")
            player.exp += monster.exp

player = Player("Player", 1000, 10, 5)
monster = Monster("Goblin", 550, 5, 5, 5)
fight = Fight(player, monster)
fight.start_fight()
print(f"{player.name} has {player.exp} xp")
