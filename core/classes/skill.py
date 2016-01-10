__author__ = 'mazzalex02'

import sys
from core.GUI import gui


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

        self.EFFECT = skill.EFFECT

    def info(self,*args):
        gui.show_skill_info(None,self)
