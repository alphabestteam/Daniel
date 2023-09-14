
import random

class Monster:

    def __init__(self, name, hero: object) -> None:
        self._name = name
        self._level = random.randint(hero.level, hero.level + 1)
        self._hp = 6 + self._level * 1.5
        self._damage = self.level + (self.level * 0.4)
        self._coin = 0
        
    @property
    def hp(self):
        return self._hp

    @property
    def damage(self):
        return self._damage

    @property
    def level(self):
        return self._level

    @property
    def max_hp(self):
        return self._max_hp

    @hp.setter
    def hp(self, life):
        self._hp = life

    @level.setter
    def level(self, level):
        self._level = level

    def reduce_health(self, hero: object):
        self.hp -= hero.damage
        if self._hp < 0:
            self.hp = 0
        return self.hp

    def attack(self, hero: object):
        hero.reduce_health(self)
