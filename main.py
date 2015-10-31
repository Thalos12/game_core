import sys
import os
import random
import time
from core.client import client
from core.classes.player import Player


class Game(object):
    def __init__(self):
        print ("\nWelcome dear adventurer! If this is your first time playing, "
               "then I welcome you and hope you will have a plesant journey. "
               "If you are already a player,then why are you still here reading "
               "this? Get out there!\n")
        name = raw_input('Insert your name, please: ')
        # noinspection PyBroadException
        try:
            open(os.path.join(root, 'data','players', name+'.profile'))
            print "Welcome back {}!".format(name)
        except:
            print "No player named {} found.".format(name)
            a = raw_input('Would you like to create a new profile?[y/n]').lower() or 'y'
            if a == 'y':
                self.create_profile(name)
            elif a == 'n':
                print "Have a good day."
            else:
                print "Sorry, this is not a valid answer."
                sys.exit()
        player = Player(self.load_profile(name))
        print "You are now ready to go.\n"
        player.info() #only while developing to make sure all is working
        
    def create_profile(self,name):
        print "Generating new stats for you."
        VIT = random.randint(10, 20)
        print "Vitality: "+str(VIT)
        time.sleep(1.5)
        STR = random.randint(1, 6)
        print "Strength: "+str(STR)
        time.sleep(1.5)
        RES = random.randint(1, 6)
        print "Resistance: "+str(RES)
        time.sleep(1.5)
        AGI = random.randint(1, 6)
        print "Agility: "+str(AGI)
        time.sleep(1.5)
        INT = random.randint(1, 6)
        print "Intelligence: "+str(INT)
        time.sleep(1.5)
        print "Your starting weapon is a short sword."
        print "Your starting armor is a tunic."
        print "You have skills at the beginning."
        stats = {}
        stats['NAME'] = name
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
        d = eval(d)
        return d

    def save_profile(self,stats):
        f = open(os.path.join(root,'data','players',stats['NAME']+'.profile'),'w')
        f.write(str(stats))

    def send_data(self, stats, target="127.0.0.1"):
        client(target, str(stats))
    
if __name__ == '__main__':
    root = os.getcwd()
    #sys.path.append(root)
    sys.path.append(os.path.join(root, 'core'))
    
    game = Game()
