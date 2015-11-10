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

        self.IMPACT_DAMAGE_MODIFIER = weapon.IMPACT_DAMAGE_MODIFIER

        self.MAGIC_DAMAGE_MODIFIER = weapon.MAGIC_DAMAGE_MODIFIER

        self.RANGED_DAMAGE_MODIFIER = weapon.RANGED_DAMAGE_MODIFIER

    def info(self):
        print "Name: {}".format(self.NAME)
        print "Kind: {}".format(self.KIND)
        print "Description: {}".format(self.DESCRIPTION)
        print "Pierce damage modifier: {}".format(self.PIERCE_DAMAGE_MODIFIER)
        print "Slash damage modifier: {}".format(self.SLASH_DAMAGE_MODIFIER)
        print "Impact damage modifier: {}".format(self.IMPACT_DAMAGE_MODIFIER)
        print "Magic damage modifier: {}".format(self.MAGIC_DAMAGE_MODIFIER)
        print "Ranged damage modifier: {}\n".format(self.RANGED_DAMAGE_MODIFIER)
