import sys
import os
import logging
import time
import battle_manager
import profiledb
import wx
from archetypes import list_archetypes
from classes.player import Player
from GUI import gui
from settings.menu_settings import *


root = os.path.dirname(os.path.realpath(__file__))
sys.path.append(root)


# noinspection PyPep8Naming
class Game(wx.Frame):
    def __init__(self, options):
        super(Game, self).__init__(parent=None, title='Children of the Goddess', size=(300,200), style=wx.MINIMIZE_BOX|wx.CLOSE_BOX)

        name = gui.ask_name(None)
        # noinspection PyBroadException
        if os.path.isfile(os.path.join(root, 'data', 'players', name + '.datafile')):
            gui.welcome_back(None, name)
        else:
            name = gui.create_new(None)
            if name == '':
                logging.info("{}".format(time.strftime("END LOG: %d %b %Y, %H:%M:%S")))
                sys.exit()
            index = gui.single_choice(None,"Please select one of the archetypes.",list_archetypes.get_list())
            if index != None:
                print 'from archetype'
                archetype = list_archetypes.get_list()[index]
            else:
                print 'something not right'
                sys.exit()
            profiledb.create(name,archetype)
            sys.exit()
        try:
            stats = profiledb.load(name)
            if stats == 'non-existent':
                gui.notification(None,'Your profile does not exist.')
                sys.exit()
            if stats == 'corrupted':
                gui.notification(None,'Your data is corrupted, delete it and start over.')
                sys.exit()
            else:
                self.player = Player(stats)
        except:
            gui.notification(None,'Your profile cannot be loaded.')
            logging.error(('Your profile cannot be loaded. This happens when the player '
                           'class has been modified in such a way that your profile no '
                           'longer has the necessary requirements to be loaded. '
                           'Delete it and start over. We are sorry for the inconvenience.'))
            sys.exit()
        logging.info("Loaded player profile.")
        gui.notification(None,'You are now ready to play!')
        # self.player.info() # used only while testing
        # self.player.weapon.info() # same as above
        # self.player.armor.info() # same as above
        sys.exit()
        self.main_menu(options)

    def main_menu(self,options):
        logging.info("Running.")

        if options['textual']:
            while True:
                s = ("*"*6 + " MAIN MENU " + "*"*6 + '\n'
                     "i - show player's info\n"
                     "w - show weapon's info\n"
                     "a - show armor's info\n"
                     "s - show skill's info\n"
                     "A - adventure mode: fight a bot\n"
                     "q - quit the game\n")
                print s
                a = raw_input("Please choose one: ")
                print '\n',
                if a=='i':
                    self.player.info()
                    time.sleep(info_sleep)
                elif a=='w':
                    self.player.weapon.info()
                    time.sleep(info_sleep)
                elif a=='a':
                    self.player.armor.info()
                    time.sleep(info_sleep)
                elif a=='s':
                    self.player.skill.info()
                    time.sleep(info_sleep)
                elif a=='A':
                    battle_manager.battle_bot(self.player)
                elif a=='q':
                    print 'Bye bye '+self.player.name+'.'
                    sys.exit()
                else:
                    print "Command is not valid.\n"
        else:
            print 'Sorry, only textual mode enabled.'
            sys.exit()


if __name__ == '__main__':
    sys.exit()
