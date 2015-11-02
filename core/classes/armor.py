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

    def info(self):
        print "Name: {}".format(self.NAME)
        print "Kind: {}".format(self.KIND)
        print "Description: {}".format(self.DESCRIPTION)
        print "Pierce damage reduce: {}".format(self.PIERCE_DAMAGE_REDUCE)
        print "Slash damage reduce: {}".format(self.SLASH_DAMAGE_REDUCE)
        print "Magic damage reduce: {}".format(self.MAGIC_DAMAGE_REDUCE)
        print "Ranged damage reduce: {}\n".format(self.RANGED_DAMAGE_REDUCE)
