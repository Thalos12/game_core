import sys
import os

root = os.getcwd()
sys.path.append(os.path.join(root, 'core'))

import core.profile as profile

name = raw_input('Insert player name, please: ')
# noinspection PyBroadException
try:
    open(os.path.join(root, 'data', 'name'))
except:
    print "No player named {} found.".format(name)
    a = raw_input('create new profile?[y/n]').lower()
    if a == 'y':
        profile.create_profile(name)
