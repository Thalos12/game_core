__author__ = 'mazzalex02'

import sys


class Skill(object):
    def __init__(self, skill_name):
        if skill_name == 'kick':
            import sample_skill_kick as skill
        else:
            print "Unknown skill."
            sys.exit()
        self.NAME = skill.NAME
        self.DESCRIPTION = skill.DESCRIPTION

        self.REQUIRED_LEVEL = skill.REQUIRED_LEVEL
        self.REQUIRED_CLASS = skill.REQUIRED_CLASS

        self.DAMAGE = skill.DAMAGE
        self.EFFECT = skill.EFFECT
