import random
import os
from archetypes.list_archetypes import *
from settings.menu_settings import *

root = os.path.dirname(os.path.realpath(__file__))

# noinspection PyDictCreation,PyDictCreation,PyDictCreation
def create(name):
    arch = raw_input('Do you want to choose one from the archetypes?[y/n][default:n]') or 'n'
    if arch == 'y':
        list_archetypes()
        archetype_name = raw_input('Archetype name: ')
        try:
            exec 'from archetypes.{} import *'.format(archetype_name)
        except:
            print 'Archetype unknown, resorting to random creation.'
            exec 'from archetypes.random import *'
    else:
        exec 'from archetypes.random import *'
    print "Generating new stats for you."
    VIT = random.randint(min_vit, max_vit)
    print "Vitality: {}".format(VIT)
    time.sleep(print_sleep)
    STR = random.randint(min_str, max_str)
    print "Strength: {}".format(STR)
    time.sleep(print_sleep)
    RES = random.randint(min_res, max_res)
    print "Resistance: {}".format(RES)
    time.sleep(print_sleep)
    AGI = random.randint(min_agi, max_agi)
    print "Agility: {}".format(AGI)
    time.sleep(print_sleep)
    INT = random.randint(min_int, max_int)
    print "Intelligence: {}".format(INT)
    time.sleep(print_sleep)
    print "Weapon: {}.".format(weapon)
    time.sleep(print_sleep)
    print "Armor: {}.".format(armor)
    time.sleep(print_sleep)
    print "Skill: {}\n".format(skill)
    time.sleep(print_sleep)

    stats = {}
    stats['NAME'] = name
    stats['LEVEL'] = 1
    stats['EXP'] = 0
    stats['MONEY'] = 10 # gold? silver? bronze? banana?
    stats['ITEMS'] = []
    stats['VIT'] = VIT
    stats['STR'] = STR
    stats['RES'] = RES
    stats['AGI'] = AGI
    stats['INT'] = INT
    stats['WEAPON'] = weapon
    stats['ARMOR'] = armor
    stats['SKILL'] = skill
    save(stats)


def load(name):
    f = open(os.path.join(root, 'data', 'players', name + '.profile'), 'r')
    d = f.readline()
    f.close()
    d = eval(d)
    return d

def save(stats):
    f = open(os.path.join(root, 'data', 'players', stats['NAME'] + '.profile'), 'w')
    f.write(str(stats))
    f.close()
    

if __name__ == '__main__':
    print __file__
    print os.getcwd()
    print os.path.dirname(os.path.realpath(__file__))
