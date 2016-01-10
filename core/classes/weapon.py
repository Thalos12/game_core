__author__ = 'mazzalex02'

import sys
from core.GUI import gui


# noinspection PyBroadException
class Weapon(object):
    def __init__(self, weapon_name):
        if ' ' in weapon_name:
            name = weapon_name.split(' ')
            weapon_name = '_'.join(name)
        try:
            exec "from core.weapons import {} as weapon".format(weapon_name)
        except:
            print "Unknown weapon."
            sys.exit()

        self.NAME = weapon.NAME
        self.KIND = weapon.KIND
        self.DESCRIPTION = weapon.DESCRIPTION

        self.PIERCE_DAMAGE_MODIFIER = weapon.PIERCE_DAMAGE_MODIFIER
        self.SLASH_DAMAGE_MODIFIER = weapon.SLASH_DAMAGE_MODIFIER
        self.IMPACT_DAMAGE_MODIFIER = weapon.IMPACT_DAMAGE_MODIFIER
        self.MAGIC_DAMAGE_MODIFIER = weapon.MAGIC_DAMAGE_MODIFIER
        self.RANGED_DAMAGE_MODIFIER = weapon.RANGED_DAMAGE_MODIFIER

    def info(self,*args):
        gui.show_weapon_info(None,self)