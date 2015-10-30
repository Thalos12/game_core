__author__ = 'mazzalex02'

import sys


# noinspection PyBroadException
class Weapon(object):
    def __init__(self, weapon_name):
        try:
            exec "from core.weapons import " + weapon_name + " as weapon"
        except:
            print "Unknown weapon."
            sys.exit()
        self.NAME = weapon.NAME
        self.KIND = weapon.KIND
        self.DESCRIPTION = weapon.DESCRIPTION

        self.PIERCE_DAMAGE_MODIFIER = weapon.PIERCE_DAMAGE_MODIFIER

        self.SLASH_DAMAGE_MODIFIER = weapon.SLASH_DAMAGE_MODIFIER

        self.MAGIC_DAMAGE_MODIFIER = weapon.MAGIC_DAMAGE_MODIFIER

        self.RANGED_DAMAGE_MODIFIER = weapon.RANGED_DAMAGE_MODIFIER
