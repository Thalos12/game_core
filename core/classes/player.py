__author__ = 'mazzalex02'
import os
import armor
import weapon
import skill
from core.GUI import gui


# import core.client as client


# noinspection PyPep8Naming
class Player(object):
    def __init__(self, stats):
        self.stats = stats
        self.weapon = weapon.Weapon(stats['WEAPON'])
        self.armor = armor.Armor(stats['ARMOR'])
        self.skill = skill.Skill(stats['SKILL'])
        self.isbot = False

    def info(self,*args):
        gui.show_player_info(None,self.stats)

    def Attack(self, target, distance):
        print '{} attacks {}.'.format(self.name,target.name)
        while True:
            if distance >= 10:
                kind = raw_input("Kind of attack?[m(agic)/r(anged)]")
            else:
                kind = raw_input("Kind of attack?[p(ierce)/s(lash)/i(mpact)/m(agic)]")
            if kind == 'p':
                if distance >=10:
                    print "You can't use this kind of attack from the distance."
                    continue
                else:
                    attack = self.stats['STR'] * self.weapon.PIERCE_DAMAGE_MODIFIER
                    defence = target.stats['RES'] * target.armor.PIERCE_DAMAGE_REDUCE
                    break
            elif kind == 's':
                if distance >= 10:
                    print "You can't use this kind of attack from the distance."
                    continue
                else:
                    attack = self.stats['STR'] * self.weapon.SLASH_DAMAGE_MODIFIER
                    defence = target.stats['RES'] * target.armor.SLASH_DAMAGE_REDUCE
                    break
            elif kind == 'i':
                if distance >= 10:
                    print "You can't use this kind of attack from the distance."
                    continue
                else:
                    attack = self.stats['STR'] * self.weapon.IMPACT_DAMAGE_MODIFIER
                    defence = target.stats['RES'] * target.armor.IMPACT_DAMAGE_REDUCE
                    break
            elif kind == 'm':
                    attack = self.stats['INT'] * self.weapon.MAGIC_DAMAGE_MODIFIER
                    defence = target.stats['RES'] * target.armor.MAGIC_DAMAGE_REDUCE
                    break
            elif kind == 'r':
                if distance <10:
                    print "You can't use this kind of attack from a close distance"
                else:
                    attack = self.stats['AGI'] * self.weapon.RANGED_DAMAGE_MODIFIER
                    defence = target.stats['RES'] * target.armor.RANGED_DAMAGE_REDUCE
                    break
            else:
                print "Kind of attack was not understood, please try again."
        # attack = round(attack,1)
        # defence = round(defence,1)
        damage = attack - defence
        if damage <= 0:
            damage = 0
        print '{} deals {} to {}.'.format(self.name,damage,target.name)
        target.stats['VIT'] -= damage
        print '{} vitality is now {}.\n'.format(target.name,target.stats['VIT'])
