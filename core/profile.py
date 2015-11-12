import random
import os

root = os.path.dirname(os.path.realpath(__file__))

# noinspection PyDictCreation,PyDictCreation,PyDictCreation
def create(name):
    print "Generating new stats for you."
    VIT = random.randint(20, 30)
    print "Vitality: " + str(VIT)
    time.sleep(print_sleep)
    STR = random.randint(1, 6)
    print "Strength: " + str(STR)
    time.sleep(print_sleep)
    RES = random.randint(1, 6)
    print "Resistance: " + str(RES)
    time.sleep(print_sleep)
    AGI = random.randint(1, 6)
    print "Agility: " + str(AGI)
    time.sleep(print_sleep)
    INT = random.randint(1, 6)
    print "Intelligence: " + str(INT)
    time.sleep(print_sleep)
    print "\nYour starting weapon is a short sword."
    time.sleep(print_sleep)
    print "Your starting armor is a tunic."
    time.sleep(print_sleep)
    print "You have no skills at the beginning.\n"
    time.sleep(print_sleep)

    stats = {}
    stats['NAME'] = name
    stats['LEVEL'] = 1
    stats['EXP'] = 0
    stats['MONEY'] = 10 # gold? silver? bronze?
    stats['ITEMS'] = []
    stats['VIT'] = VIT
    stats['STR'] = STR
    stats['RES'] = RES
    stats['AGI'] = AGI
    stats['INT'] = INT
    stats['WEAPON'] = 'short_sword'
    stats['ARMOR'] = 'tunic'
    stats['SKILL'] = 'no_skill'
    save_profile(stats)


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
