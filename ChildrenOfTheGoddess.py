import os
import logging
import time
import argparse
import ConfigParser
import wx
from core import main_menu

_version = 'pre-alpha2'
_name = 'Children of the Goddess'
_author = ['Alessandro Mazzi - Programmer',
           'Giada Faraon - Programmer',
           'Giovanni Muranetto - Programmer',
           'Linda Faraon - Artist']

# read command line options
arg_parser = argparse.ArgumentParser(description='Start the game "Children of the Goddess".')
arg_parser.add_argument('--mute',
                        help="Disable sound and music.",
                        default=False,
                        action='store_true')
args = arg_parser.parse_args()
options = {}
options['mute'] = args.mute

cfg_parser = ConfigParser.SafeConfigParser()
cfg_parser.read('configs.cfg')
for s in cfg_parser.sections():
    for o in cfg_parser.options(s):
        options[str(o)] = cfg_parser.get(s, o, 0)

print options

# start logging
logging.basicConfig(filename=os.path.join('core', 'logs', str(int(time.time())) + '.txt'),
                    level=logging.DEBUG)
logging.info("{}".format(time.strftime("Started logging %d %b %Y, %H:%M:%S")))
logging.info("\"Children of the Goddess\" version is {}".format(_version))

options_for_log = str()
print sorted(options.keys(), cmp=None, key=None, reverse=False)
for k in sorted(options.keys()):
    options_for_log + str(k[0].upper()) + str(k[1:]) + ': ' + str(options[k])
print options_for_log
# logging.info("Mute is set to {}.".format(options['mute']))
logging.info(options_for_log)

# start the actual game
app = wx.App(False)
frame = main_menu.Game(options)
app.MainLoop()
