__author__ = 'mazzalex02'

import sys


# noinspection PyBroadException
class Armor(object):
    def __init__(self, armor_name):
        try:
            exec "from core.armors import " + armor_name + " as armor"
        except:
            print "Unknown armor."
            sys.exit()
        self.NAME = armor.NAME
        self.KIND = armor.KIND
        self.DESCRIPTION = armor.DESCRIPTION

        self.PIERCE_DAMAGE_REDUCE = armor.PIERCE_DAMAGE_REDUCE

        self.SLASH_DAMAGE_REDUCE = armor.SLASH_DAMAGE_REDUCE

        self.MAGIC_DAMAGE_REDUCE = armor.MAGIC_DAMAGE_REDUCE

        self.RANGED_DAMAGE_REDUCE = armor.RANGED_DAMAGE_REDUCE
