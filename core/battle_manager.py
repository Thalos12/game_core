__author__ = 'mazzalex02'
import class_player as class_player
import class_enemy as class_enemy
import class_weapon as class_weapon
import class_armor
import random


# noinspection PyPep8Naming
def Fight(unit1, unit2):
    if unit1.AGILITY > unit2.AGILITY:
        print unit1.NAME, "attacks first."
        unit1.Attack(unit2)
        if unit2.VITALITY > 0:
            print unit2.NAME, "attacks."
            unit2.Attack(unit1)
            if unit1.VITALITY < 0:
                print unit1.MOVEMENT, 'is dead.'
        else:
            print unit2.NAME, "is dead."
    else:
        print unit2.NAME, "attacks first."
        unit2.Attack(unit1)
        if unit1.VITALITY > 0:
            print unit1.NAME, "attacks."
            unit1.Attack(unit2)
            if unit2.VITALITY < 0:
                print unit2.NAME, 'is dead.'
        else:
            print unit1.NAME, "is dead."


if __name__ == '__main__':
    player = class_player.Player({"NAME": "Leo",
                                  "DESCRIPTION": "Me.",
                                  "VITALITY": 30,
                                  "STRENGTH": 7,
                                  "RESISTANCE": 5,
                                  "AGILITY": 3,
                                  "INTELLIGENCE": 5,
                                  "WEAPON": class_weapon.Weapon('sword'),
                                  "ARMOR": class_armor.Armor('tunic'),
                                  "SKILL": None})

    enemy = class_enemy.Enemy()

    Fight(player, enemy)
