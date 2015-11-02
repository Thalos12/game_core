__author__ = 'mazzalex02'
import os
import armor
import weapon
import skill
#import core.client as client


# noinspection PyPep8Naming
class Player(object):
    def __init__(self, stats):
        self.stats = stats
        self.name = stats['NAME']
        self.weapon = weapon.Weapon(stats['WEAPON'])
        self.armor = armor.Armor(stats['ARMOR'])
        #self.skill = skill.Skill(stats['SKILL'])

    def Attack(self, target):
        print self.name, 'attacks', target.name, '.'
        while True:
            kind = raw_input("Kind of attack?[p(ierce)/s(lash)/m(agic)/r(anged)]")
            if kind == 'p':
                damage = (self.stats['STR'] * self.weapon.PIERCE_DAMAGE_MODIFIER - target.stats['RES'] * target.armor.PIERCE_DAMAGE_REDUCE)
                break
            elif kind == 's':
                damage = (self.stats['STR'] * self.weapon.SLASH_DAMAGE_MODIFIER - target.stats['RES'] * target.armor.SLASH_DAMAGE_REDUCE)
                break
            elif kind == 'm':
                damage = (self.stats['STR'] * self.weapon.MAGIC_DAMAGE_MODIFIER - target.stats['RES'] * target.armor.MAGIC_DAMAGE_REDUCE)
                break
            elif kind == 'r':
                damage = (self.stats['STR'] * self.weapon.RANGED_DAMAGE_MODIFIER - target.stats['RES'] * target.armor.RANGED_DAMAGE_REDUCE)
                break
            else:
                print "Kind of attack was not understood, please try again."
        if damage <= 0:
            damage = 0
        print self.name, 'deals', damage, 'damage to', target.name
        target.stats['VIT'] -= damage
        print target.name, 'vitality is now', target.stats['VIT']

    def info(self):
        l = ["Name","Vit","Str","Res","Agi","Int","Weapon","Armor","Skill"]
        print "Player info."
        for element in l:
            value = self.stats[element.upper()]
            if "_" in str(value):
                value = "{} {}".format(value.split("_")[0],value.split("_")[1])
            print "{} : {}".format(element,value)
        print ''

    
