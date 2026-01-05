class Character:
    def __init__(self, name, hp):
        self.name = name
        self._hp = 0
        self.hp = hp

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        elif value > 100:
            self._hp = 100
        else:
            self._hp = value

    def take_damage(self, amount):
        self.hp = self.hp - amount

    def heal(self, amount):
        self.hp = self.hp + amount

    def status(self):
        print(f"{self.name}: HP = {self.hp}")


hero = Character("Batman", 80)

hero.take_damage(30)
hero.status()

hero.heal(40)
hero.status()

hero.take_damage(200)
hero.status()
