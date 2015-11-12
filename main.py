import logging
import os
import random
import sys
import time

from core import battle_manager, update
from core.classes.bot import Bot
from core.classes.player import Player
from core.client import client
from core.settings.settings import *

sys.path.append(os.getcwd())

# start logging
logging.basicConfig(filename=os.path.join('core', 'logs', str(int(time.time())) + '.txt'), level=logging.DEBUG)
logging.info("{}".format(time.strftime("Started logging %d %b %Y, %H:%M:%S")))

# noinspection PyPep8Naming
class Game(object):
    def __init__(self):
        print ("\nWelcome dear adventurer! If this is your first time playing, "
               "then I welcome you and hope you will have a pleasant journey. "
               "If you are already a player,then why are you still here reading "
               "this? Get out there!\n")

        name = raw_input('Insert your name, please: ')
        # noinspection PyBroadException
        try:
            open(os.path.join(root, 'core', 'data', 'players', name + '.profile'))
            print "\nWelcome back {}!\n".format(name)
        except:
            print "\nNo player named {} found.\n".format(name)
            a = raw_input('Would you like to create a new profile?[y/n]').lower() or 'y'
            if a == 'y':
                self.create_profile(name)
            elif a == 'n':
                print "Have a good day."
                logging.info("{}".format(time.strftime("END LOG: %d %b %Y, %H:%M:%S")))
                sys.exit()
            else:
                print "Sorry, this is not a valid answer."
                logging.info("{}".format(time.strftime("END LOG: %d %b %Y, %H:%M:%S")))
                sys.exit()
        self.player = Player(self.load_profile(name))
        try:
            self.player = Player(self.load_profile(name))
        except:
            print 'Your profile cannot be loaded.'
            logging.error(('Your profile cannot be loaded. This happens when the player '
                           'class has been modified in such a way that your profile no '
                           'longer has the necessary requirements to be loaded. '
                           'Delete it and start over. We are sorry for the inconvenience.'))
            sys.exit()
        logging.info("Loaded player profile.")
        print "You are now ready to go!\n"
        # self.player.info() # used only while testing
        # self.player.weapon.info() # same as above
        # self.player.armor.info() # same as above
        self.run()

    def run(self):
        logging.info("Running.")
        while True:
            opt = self.show_main_menu()
            a = raw_input("Please choose one: ")
            print '\n'
            if a in opt.keys():
                exec opt[a]
            else:
                print "Command is not valid.\n"

    def battle(self):
        bot = Bot(self.load_bot('bot'))
        battle_manager.Battle_menu(self.player, bot)

    # noinspection PyDictCreation,PyDictCreation,PyDictCreation
    def create_profile(self, name):
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
        self.save_profile(stats)

    def load_profile(self, name):
        f = open(os.path.join(root, 'core', 'data', 'players', name + '.profile'), 'r')
        d = f.readline()
        f.close()
        d = eval(d)
        return d

    def save_profile(self, stats):
        f = open(os.path.join(root, 'core', 'data', 'players', stats['NAME'] + '.profile'), 'w')
        f.write(str(stats))
        f.close()

    def load_bot(self, name):
        try:
            exec "from core.bots import {} as bot".format(name)
        except:
            print "Bot was not found."
        return {'NAME': bot.NAME,
                'DESCRIPTION': bot.DESCRIPTION,
                'LEVEL': bot.LEVEL,
                'EXP': bot.EXP,
                'MONEY':bot.MONEY,
                'ITEMS':bot.ITEMS,
                'VIT': bot.VITALITY,
                'STR': bot.STRENGTH,
                'RES': bot.RESISTANCE,
                'AGI': bot.AGILITY,
                'INT': bot.INTELLIGENCE,
                'WEAPON': bot.WEAPON,
                'ARMOR': bot.ARMOR,
                'SKILL': bot.SKILL}

    def send_data(self, stats, target="127.0.0.1"):
        client(target, str(stats))

    def show_main_menu(self):
        opt = {"i": "self.player.info();raw_input('Press enter.')",
               "w": "self.player.weapon.info();raw_input('Press enter.')",
               "a": "self.player.armor.info();raw_input('Press enter.')",
               "A": "self.battle()",
               "q": "print 'Bye bye '+self.player.name+'.';sys.exit()"}
        s = ("*" * 6 + "MAIN MENU" + "*" * 6 + '\n'
             "i - show player's info\n"
             "w - show weapon's info\n"
             "a - show armor's info\n"
             "A - adventure mode: fight a bot\n"
             "q - quit the game\n")
        print s
        return opt


if __name__ == '__main__':
    root = os.getcwd()
    # sys.path.append(root)
    sys.path.append(os.path.join(root, 'core'))

    check = raw_input('Check for updates?[y,n]').lower()
    if check == 'y':
        time.sleep(1)
        update.update()

    game = Game()
