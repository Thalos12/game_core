__author__ = 'mazzalex02'

import sys


class Skill(object):
    def __init__(self, skill_name):
        if ' ' in skill_name:
            name = skill_name.split(' ')
            #print name
            skill_name = '_'.join(name)
            #print skill_name
        try:
            exec "from core.skills import " + skill_name + " as skill"
        except:
            print "Unknown skill."
            sys.exit()
        self.NAME = skill.NAME
        self.DESCRIPTION = skill.DESCRIPTION

        self.REQUIRED_LEVEL = skill.REQUIRED_LEVEL
        self.REQUIRED_CLASS = skill.REQUIRED_CLASS

        self.DAMAGE = skill.DAMAGE
        self.EFFECT = skill.EFFECT

    def info(self):
        print "Name: {}".format(self.NAME)
        print "Description: {}".format(self.DESCRIPTION)
        print "Damage: {}".format(self.DAMAGE)
        print "Effects: {}\n".format(self.EFFECT)
