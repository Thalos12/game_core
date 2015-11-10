__author__ = 'mazzalex02'

import player
import random


# NOTE: the "stats" have to be loaded by main.py -> bots have to be created by it
# noinspection PyPep8Naming
class Bot(player.Player):
    def __init__(self, stats):
        super(Bot, self).__init__(stats)
        self.isbot = True

    def bot_Attack(self, target, distance):
        if distance >= 10:
            attacks = ['magic', 'ranged']
        else:
            attacks = ['pierce', 'slash', 'impact', 'magic']
        i = random.randint(0, len(attacks) - 1)
        a = attacks[i]
        print "{} attacks with {}.".format(self.name, a)
        if a == 'pierce':
            attack = self.stats['STR'] * self.weapon.PIERCE_DAMAGE_MODIFIER
            defence = target.stats['RES'] * target.armor.PIERCE_DAMAGE_REDUCE
        elif a == 'slash':
            attack = self.stats['STR'] * self.weapon.SLASH_DAMAGE_MODIFIER
            defence = target.stats['RES'] * target.armor.SLASH_DAMAGE_REDUCE
        elif a == 'impact':
            attack = self.stats['STR'] * self.weapon.IMPACT_DAMAGE_MODIFIER
            defence = target.stats['RES'] * target.armor.IMPACT_DAMAGE_REDUCE
        elif a == 'magic':
            attack = self.stats['INT'] * self.weapon.MAGIC_DAMAGE_MODIFIER
            defence = target.stats['RES'] * target.armor.MAGIC_DAMAGE_REDUCE
        elif a == 'ranged':
            attack = self.stats['AGI'] * self.weapon.RANGED_DAMAGE_MODIFIER
            defence = target.stats['RES'] * target.armor.RANGED_DAMAGE_REDUCE
        damage = attack - defence
        if damage <= 0:
            damage = 0
        print "{} deals {} to {}.".format(self.name, damage, target.name)
        target.stats['VIT'] -= damage
        print "{} vitality is now {}.\n".format(target.name, target.stats['VIT'])
