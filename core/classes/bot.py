__author__ = 'mazzalex02'

import player
import random

#NOTE: the "stats" have to be loaded by the main.py -> bots have to be created by it
class Bot(player.Player):
    def __init__(self,stats):
        super(Bot, self).__init__(stats)
        self.isbot = True
    def bot_Attack(self,target,distance):
        if distance >= 10:
            attacks = ['magic','ranged']
        else:
            attacks = ['pierce','slash','magic','ranged']
        i = random.randint(0,len(attacks)-1)
        a = attacks[i]
        print "{} attacks with magic.".format(self.name)
        if a == 'pierce':
            damage = self.stats['STR']*self.weapon.PIERCE_DAMAGE_MODIFIER - target.stats['RES']*target.armor.PIERCE_DAMAGE_REDUCE
        elif a == 'slash':
            damage = self.stats['STR']*self.weapon.SLASH_DAMAGE_MODIFIER - target.stats['RES']*target.armor.SLASH_DAMAGE_REDUCE
        elif a == 'magic':
            damage = self.stats['INT']*self.weapon.MAGIC_DAMAGE_MODIFIER - target.stats['RES']*target.armor.MAGIC_DAMAGE_REDUCE
        elif a == 'ranged':
            damage = self.stats['STR']*self.weapon.RANGED_DAMAGE_MODIFIER - target.stats['RES']*target.armor.RANGED_DAMAGE_REDUCE
        if damage <=0:
            damage = 0
        print "{} deals {} to {}".format(self.name,damage,target.name)
        target.stats['VIT'] -= damage
        print "{} vitality is now {}\n".format(target.name,target.stats['VIT'])