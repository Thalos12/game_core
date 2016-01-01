_version = 'pre-alpha1'

import sys
import os
import logging
import time
import ConfigParser
from core import main

def boot():
    # start logging
    logging.basicConfig(filename=os.path.join('core', 'logs', str(int(time.time())) + '.txt'), level=logging.DEBUG)
    logging.info("{}".format(time.strftime("Started logging %d %b %Y, %H:%M:%S")))
    logging.info("game_core version is {}".format(_version))

    # load basic configurations
    options={}
    config = ConfigParser.ConfigParser()
    config.read('options.cfg')
    textual = config.get('MODE','textual')
    logging.info("Textual mode is set to {}.".format(textual))
    options['textual'] = textual
    volume = config.get('AUDIO','volume')
    logging.info("Audio volume is set to {}.".format(volume))
    options['volume'] = volume

    main.Game(options)



if __name__ == '__main__':
    boot()
