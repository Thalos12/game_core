import sys
import os
import random
import time
from core.client import client
from core.classes.player import Player
from core.settings.settings import *


class Game(object):
    def __init__(self):
        print ("\nWelcome dear adventurer! If this is your first time playing, "
               "then I welcome you and hope you will have a plesant journey. "
               "If you are already a player,then why are you still here reading "
               "this? Get out there!\n")
        name = raw_input('Insert your name, please: ')
        # noinspection PyBroadException
        try:
            open(os.path.join(root,'data','players', name+'.profile'))
            print "\nWelcome back {}!\n".format(name)
        except:
            print "\nNo player named {} found.\n".format(name)
            a = raw_input('Would you like to create a new profile?[y/n]').lower() or 'y'
            if a == 'y':
                self.create_profile(name)
            elif a == 'n':
                print "Have a good day."
            else:
                print "Sorry, this is not a valid answer."
                sys.exit()
        self.player = Player(self.load_profile(name))
        print "You are now ready to go!\n"
        #self.player.info() # used only while testing
        #self.player.weapon.info() # same as above
        #self.player.armor.info() # same as above
        self.run()

    def run(self):
        while True:
            opt = self.show_main_menu()
            a = raw_input("Please choose one: ")
            print '\n'
            if a in opt.keys():
                exec opt[a]
            else:
                print "Command is not valid.\n"
        
    def create_profile(self,name):
        print "Generating new stats for you."
        VIT = random.randint(10, 20)
        print "Vitality: "+str(VIT)
        time.sleep(print_sleep)
        STR = random.randint(1, 6)
        print "Strength: "+str(STR)
        time.sleep(print_sleep)
        RES = random.randint(1, 6)
        print "Resistance: "+str(RES)
        time.sleep(print_sleep)
        AGI = random.randint(1, 6)
        print "Agility: "+str(AGI)
        time.sleep(print_sleep)
        INT = random.randint(1, 6)
        print "Intelligence: "+str(INT)
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
        stats['VIT'] = VIT
        stats['STR'] = STR
        stats['RES'] = RES
        stats['AGI'] = AGI
        stats['INT'] = INT
        stats['WEAPON'] = 'short_sword'
        stats['ARMOR'] = 'tunic'
        stats['SKILL'] = 'no_skill'
        self.save_profile(stats)

    def load_profile(self,name):
        f = open(os.path.join(root,'data','players',name+'.profile'),'r')
        d = f.readline()
        f.close()
        d = eval(d)
        return d

    def save_profile(self,stats):
        f = open(os.path.join(root,'data','players',stats['NAME']+'.profile'),'w')
        f.write(str(stats))
        f.close()

    def send_data(self, stats, target="127.0.0.1"):
        client(target, str(stats))

    def show_main_menu(self):
        opt = {"i":"self.player.info()",
               "w":"self.player.weapon.info()",
               "a":"self.player.armor.info()",
               "q":"print 'Bye bye '+self.player.name+'.';sys.exit()"}
        s = ("*"*6+"MAIN MENU"+"*"*6+'\n'
             "i - show player's info\n"
             "w - show weapon's info\n"
             "a - show armor's info\n"
             "q - quit the game\n")
        print s
        return opt
    
if __name__ == '__main__':
    root = os.getcwd()
    #sys.path.append(root)
    sys.path.append(os.path.join(root, 'core'))
    
    game = Game()
