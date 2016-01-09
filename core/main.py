import sys
import os
import logging
import time
import battle_manager
import update
import profile
import wx
from classes.player import Player
from settings.menu_settings import *

root = os.path.dirname(os.path.realpath(__file__))
#print root
sys.path.append(root)

# noinspection PyPep8Naming
class Game(wx.Frame):
    def __init__(self,options):

        super(Game, self).__init__(parent=None, title='Children of the Goddess',size=(300,200),style=wx.MINIMIZE_BOX|wx.CLOSE_BOX)
        
        if options['textual']:
            print ("\nWelcome dear adventurer! If this is your first time playing, "
                   "\nthen I welcome you and hope you will have a pleasant journey. "
                   "\nIf you are already a player,then why are you still here reading "
                   "\nthis? Get out there!\n")
            name = raw_input('==> Insert your name, please: ')
        else:
            name = self.ask_name()
        # noinspection PyBroadException
        try:
            open(os.path.join(root, 'data', 'players', name + '.profile'))
            if options['textual']:
                print "\nWelcome back {}!\n".format(name)
        except:
            if options['textual']:
                print "\nNo player named {} found.\n".format(name)
                a = raw_input('Would you like to create a new profile?[y/n]').lower() or 'y'
            else:
                sys.exit()
            if a == 'y':
                profile.create(name)
            elif a == 'n':
                if options['textual']:
                    print "Have a good day."
                logging.info("{}".format(time.strftime("END LOG: %d %b %Y, %H:%M:%S")))
                sys.exit()
            else:
                if options['textual']:
                    print "Sorry, this is not a valid answer."
                logging.info("{}".format(time.strftime("END LOG: %d %b %Y, %H:%M:%S")))
                sys.exit()
        try:
            self.player = Player(profile.load(name))
        except:
            if options['textual']:
                print 'Your profile cannot be loaded.'
            logging.error(('Your profile cannot be loaded. This happens when the player '
                           'class has been modified in such a way that your profile no '
                           'longer has the necessary requirements to be loaded. '
                           'Delete it and start over. We are sorry for the inconvenience.'))
            sys.exit()
        logging.info("Loaded player profile.")
        if options['textual']:
            print "You are now ready to go!\n"
        # self.player.info() # used only while testing
        # self.player.weapon.info() # same as above
        # self.player.armor.info() # same as above
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

    def ask_name(self):
        ask = wx.TextEntryDialog(self,message='Name check.',caption='Cheking your name.',style=wx.OK,pos=(200,150))
        ask.ShowModal()
        name = ask.GetValue()
        ask.Destroy()
        return name


if __name__ == '__main__':
    sys.exit()