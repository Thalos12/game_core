import logging
import os
import random
import sys
import time
import ConfigParser

from core import battle_manager
from core import update
from core import profile
from core.classes.bot import Bot
from core.classes.player import Player
from core.settings.menu_settings import *

sys.path.append(os.getcwd())

_version = 'pre-alpha1'

# start logging
logging.basicConfig(filename=os.path.join('core', 'logs', str(int(time.time())) + '.txt'), level=logging.DEBUG)

logging.info("{}".format(time.strftime("Started logging %d %b %Y, %H:%M:%S")))
logging.info("game_core version is {}".format(_version))

# load basic configurations
config = ConfigParser.ConfigParser()
config.read('game_core.cfg')
textual = config.get('MODE','textual')
logging.info("Textual mode is set to {}.".format(textual))
volume = config.get('AUDIO','volume')
logging.info("Audio volume is set to {}.".format(volume))

# noinspection PyPep8Naming
class Game(object):
    def __init__(self):
        if textual:
            print ("\nWelcome dear adventurer! If this is your first time playing, "
                   "then I welcome you and hope you will have a pleasant journey. "
                   "If you are already a player,then why are you still here reading "
                   "this? Get out there!\n")
            name = raw_input('Insert your name, please: ')
            
        # noinspection PyBroadException
        try:
            open(os.path.join(root, 'core', 'data', 'players', name + '.profile'))
            if textual:
                print "\nWelcome back {}!\n".format(name)
        except:
            if textual:
                print "\nNo player named {} found.\n".format(name)
                a = raw_input('Would you like to create a new profile?[y/n]').lower() or 'y'
            else:
                sys.exit()
            if a == 'y':
                profile.create(name)
            elif a == 'n':
                if textual:
                    print "Have a good day."
                logging.info("{}".format(time.strftime("END LOG: %d %b %Y, %H:%M:%S")))
                sys.exit()
            else:
                if textual:
                    print "Sorry, this is not a valid answer."
                logging.info("{}".format(time.strftime("END LOG: %d %b %Y, %H:%M:%S")))
                sys.exit()
        try:
            self.player = Player(profile.load(name))
        except:
            if textual:
                print 'Your profile cannot be loaded.'
            logging.error(('Your profile cannot be loaded. This happens when the player '
                           'class has been modified in such a way that your profile no '
                           'longer has the necessary requirements to be loaded. '
                           'Delete it and start over. We are sorry for the inconvenience.'))
            sys.exit()
        logging.info("Loaded player profile.")
        if textual:
            print "You are now ready to go!\n"
        # self.player.info() # used only while testing
        # self.player.weapon.info() # same as above
        # self.player.armor.info() # same as above
        self.run()

    def run(self):
        logging.info("Running.")
        while True:
            if textual:
                opt = self.show_main_menu()
                a = raw_input("Please choose one: ")
                print '\n',
            if a in opt.keys():
                exec opt[a]
            else:
                if textual:
                    print "Command is not valid.\n"

    def show_main_menu(self):
        opt = {"i": "self.player.info();time.sleep(info_sleep)",
               "w": "self.player.weapon.info();time.sleep(info_sleep)",
               "a": "self.player.armor.info();time.sleep(info_sleep)",
               "s": "self.player.skill.info();time.sleep(info_sleep)",
               "A": "battle_manager.battle_bot(self.player)",
               "q": "print 'Bye bye '+self.player.name+'.';sys.exit()"}
        s = ("*"*6 + " MAIN MENU " + "*"*6 + '\n'
             "i - show player's info\n"
             "w - show weapon's info\n"
             "a - show armor's info\n"
             "s - show skill's info\n"
             "A - adventure mode: fight a bot\n"
             "q - quit the game\n")
        print s
        return opt


if __name__ == '__main__':
    root = os.getcwd()
    # sys.path.append(root)
    sys.path.append(os.path.join(root, 'core'))
    if textual:
        check = raw_input('Check for updates?[y,n][default:n]').lower() or 'n'
    if check == 'y':
        if textual:
            print '\n',
        update.update()

    game = Game()
