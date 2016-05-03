import os
import argparse
import ConfigParser
import wx
from core import main_menu
# from core import main_menu_dev

# fundamental informations
_version = 'pre-alpha2'
_name = 'Children of the Goddess'
_author = ['Alessandro Mazzi - Programmer',
           'Giada Faraon - Programmer',
           'Giovanni Muranetto - Programmer',
           'Linda Faraon - Artist']
_root = os.path.dirname(os.path.realpath(__file__))

# read command line options
arg_parser = argparse.ArgumentParser(description='Start the game "Children of the Goddess".')
arg_parser.add_argument('--mute',
                        help="Disable sound and music.",
                        default=False,
                        action='store_true')
args = arg_parser.parse_args()
options = {}
options['mute'] = args.mute

# read configuration file
cfg_parser = ConfigParser.SafeConfigParser()
cfg_parser.read('configs.cfg')
for s in cfg_parser.sections():
    for opt in cfg_parser.options(s):
        options[str(opt)] = cfg_parser.get(s, opt, 0)

# start the actual game
app = wx.App(False)
frame = main_menu.Game(options)
app.MainLoop()
