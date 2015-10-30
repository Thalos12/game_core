__author__ = 'mazzalex02'

import core.classes.weapon
import core.classes.skill

import sys


# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic,PyPep8Naming
class Unit(object):
    def __init__(self, KIND, NAME):
        if KIND == 'soldier':
            import sample_unit_soldier as unit_class
        else:
            print "Unknown unit."
            sys.exit()
        self.NAME = NAME
        self.CLASS = unit_class.CLASS
        self.DESCRIPTION = unit_class.DESCRIPTION

        self.VITALITY = unit_class.VITALITY
        self.RECOVERY = unit_class.RECOVERY

        self.MANA = unit_class.MANA
        self.CONCENTRATION = unit_class.CONCENTRATION

        self.PHYSICAL_ATTACK = unit_class.PHYSICAL_ATTACK
        self.PHYSICAL_DEFENCE = unit_class.PHYSICAL_DEFENCE

        self.RANGED_ATTACK = unit_class.RANGED_ATTACK
        self.RANGED_DEFENCE = unit_class.RANGED_DEFENCE

        self.MAGIC_ATTACK = unit_class.MAGIC_ATTACK
        self.MAGIC_DEFENSE = unit_class.MAGIC_DEFENSE

        self.MOVEMENT = unit_class.MOVEMENT

        self.SKILLS = self.get_skills(unit_class.SKILLS)

        self.WEAPON = self.get_weapon(unit_class.WEAPON)

    def get_skills(self, skill_name):
        return core.classe.skill.Skill(skill_name)

    def get_weapon(self, weapon_name):
        return core.classes.weapon.Weapon(weapon_name)

    def Attack(self, target):
        pass

# unit = Unit('soldier','Nessuno')
