LIFE_HEAL = 0.20
DAMAGE = 0.5
NECC_COINS = 1.5

def prec_calculate(num: int, precent: int):
    result = (num // 100) * precent
    return result


class Hero:
    def __init__(self, name) -> None:
        self._name = name
        self._hp = 10
        self._max_hp = 10
        self._damage = 2
        self._level = 1
        self._coin = 0

    @property
    def coin(self):
        return self._coin

    @property
    def level(self):
        return self._level

    @property
    def damage(self):
        return self._damage

    @property
    def hp(self):
        return self._hp

    @property
    def max_hp(self):
        return self._max_hp

    @coin.setter
    def coin(self, value):
        self._coin = value

    @level.setter
    def level(self, value):
        self._level = value

    @damage.setter
    def damage(self, value):
        self._damage = value

    @hp.setter
    def hp(self, value):
        self._hp = value

    @max_hp.setter
    def max_hp(self, value):
        self._max_hp = value

    def heal(self):
        self._hp += self._max_hp * LIFE_HEAL
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    def level_up(self):
        if self._coin >= self._level * NECC_COINS:
            self._coin -= self._level * NECC_COINS
            self._max_hp += prec_calculate(self._max_hp, DAMAGE)
            self._hp = self._max_hp
            self._level += 1
            self._damage += self._damage * DAMAGE

            return 
        else:
            return print("You don't have enough coins!\n")

    def defend(self, monster: object):
        self._hp -= monster.damage * 0.2

    def reduce_health(self, monster):
        self._hp -= monster.damage
        if self._hp <= 0:
            self._hp = 0
        return self._hp

    def increase_coins(self, coin):
        self.coin += coin

    def attack(self, monster: object):
        monster.hp -= self._damage
        if monster.hp <= 0:
            self.increase_coins(monster.level)
