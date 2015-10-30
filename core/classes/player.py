__author__ = 'mazzalex02'
import os
import armor
import weapon
import core.client as client


# noinspection PyPep8Naming
class Player(object):
    def __init__(self, stats):
        self.NAME = stats["NAME"]  # max 15
        self.DESCRIPTION = stats["DESCRIPTION"]  # max 35

        self.VITALITY = stats["VITALITY"]
        self.STRENGTH = stats["STRENGTH"]
        self.RESISTANCE = stats["RESISTANCE"]
        self.AGILITY = stats["AGILITY"]
        self.INTELLIGENCE = stats["INTELLIGENCE"]

        self.WEAPON = stats["WEAPON"]
        self.ARMOR = stats["ARMOR"]

        self.SKILL = stats["SKILL"]

    def Attack(self, target):
        print self.NAME, 'attacks', target.NAME, '.'
        while True:
            kind = raw_input("Kind of attack?[p(ierce)/s(lash)/m(agic)/r(anged)]")
            if kind == 'p':
                damage = (self.STRENGTH * self.WEAPON.PIERCE_DAMAGE_MODIFIER - target.RESISTANCE * target.ARMOR.PIERCE_DAMAGE_REDUCE)
                break
            elif kind == 's':
                damage = (self.STRENGTH * self.WEAPON.SLASH_DAMAGE_MODIFIER - target.RESISTANCE * target.ARMOR.SLASH_DAMAGE_REDUCE)
                break
            elif kind == 'm':
                damage = (self.STRENGTH * self.WEAPON.MAGIC_DAMAGE_MODIFIER - target.RESISTANCE * target.ARMOR.MAGIC_DAMAGE_REDUCE)
                break
            elif kind == 'r':
                damage = (self.STRENGTH * self.WEAPON.RANGED_DAMAGE_MODIFIER - target.RESISTANCE * target.ARMOR.RANGED_DAMAGE_REDUCE)
                break
            else:
                print "Kind of attack was not understood, please try again."
        if damage <= 0:
            damage = 0
        print self.NAME, 'deals', damage, 'damage to', target.NAME
        target.VITALITY -= damage
        print target.NAME, 'vitality is now', target.VITALITY

    def send_data(self, target="127.0.0.1"):
        data = {'NAME': self.NAME, 'DESCRIPTION': self.DESCRIPTION, 'VITALITY': self.VITALITY,
                'STRENGTH': self.STRENGTH, 'RESISTANCE': self.INTELLIGENCE, 'AGILITY': self.AGILITY,
                'INTELLIGENCE': self.INTELLIGENCE, 'WEAPON': self.WEAPON, 'ARMOR': self.ARMOR, 'SKILL': self.SKILL}
        client.client(target, str(data))

    def save(self,name):
        open(os.path.join(root)


if __name__ == '__main__':
    player = Player({"NAME": "Leo",
                     "DESCRIPTION": "Me.",
                     "VITALITY": 30,
                     "STRENGTH": 7,
                     "RESISTANCE": 5,
                     "AGILITY": 3,
                     "INTELLIGENCE": 5,
                     "WEAPON": 'sword',
                     "ARMOR": 'tunic',
                     "SKILL": None})

    # enemy = enemy.Enemy()

    # player.send_data()

    # player.Attack(enemy)
