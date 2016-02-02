_version = 'pre-alpha1'

import sys
import os
import logging
import time
import argparse
import wx
from core import main, main2

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
logging.info("Audio mute is set to {}.".format(options['mute']))


app = wx.App(False)
#frame = main.Game(options)
frame = main2.Game(options)
app.MainLoop()