import random
import os

# noinspection PyPep8Naming
def create_profile(name):
    print "Generating new stats"
    VIT = random.randint(10, 20)
    STR = random.randint(1, 6)
    RES = random.randint(1, 6)
    AGI = random.randint(1, 6)
    INT = random.randint(1, 6)
    print VIT, STR, RES, AGI, INT
    stats = [VIT, STR, RES, AGI, INT]
    stats.append(['sword','tunic',None])
    save_profile(stats)

def load_profile(name):
    f = open(os.path.join(root,'data','players',name+'.profile'),'r')
    print f.readline()

def save_profile(stats):
    f = open(os.path.join(root,'data','players',name+'.profile'),'w')
    f.write(stats)
    
if __name__ == '__main__':
    create_profile('pippo')
