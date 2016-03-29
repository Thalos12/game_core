_version = 'pre-alpha1'

import os
import logging
import time
import argparse
import wx
from core import main

# read options
parser = argparse.ArgumentParser(description='Start the game "Children of the Goddess".')
parser.add_argument('--mute',help="Disable sound and music.",default=False,action='store_true')
args = parser.parse_args()
options={}
options['mute'] = args.mute

# start logging
logging.basicConfig(filename=os.path.join('core', 'logs', str(int(time.time())) + '.txt'), level=logging.DEBUG)
logging.info("{}".format(time.strftime("Started logging %d %b %Y, %H:%M:%S")))
logging.info("\"Children of the Goddess\" version is {}".format(_version))
logging.info("Mute is set to {}.".format(options['mute']))

# start the main
app = wx.App(False)
#frame = main.Game(options)
frame = main.Game(options)
app.MainLoop()