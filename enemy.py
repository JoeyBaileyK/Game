class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class Guard(Enemy):
    def __init__(self):
        super().__init__(name="Guard", hp=20, damage=4)

class Townman(Enemy):
    def __init__(self):
        super().__init__(name="Guard", hp=1, damage=0)



