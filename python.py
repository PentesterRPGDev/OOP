class Monster:
    def __init__(self, name, hp, atk, dmg, exp):
        self.name = name
        self.health = hp
        self.attack = atk
        self.damage = dmg
        self.exp = exp

    def __str__(self):
        return f"{self.name} has {self.health} hp."

    def check_health(self):
        if self.health > 0:
            print(f"{self.name} has {self.health}hp left.")
        else:
            print(f"you've killed the {self.name}")
    
    def fight(self, name)
    while check_health:
        print("fighting")    

class Goblin(Monster):
    def __init__(self, name, hp, atk, dmg, exp):
        super().__init__(name, hp, atk, dmg, exp)

class Spider(Monster):
    pass

goblin = Goblin("goblin", 550, 5, 5, 5)
spider = Spider("Spider", 300, 3, 3, 3)
goblin.check_health()
spider.check_health()
