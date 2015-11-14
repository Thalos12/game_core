import os,time
from os import listdir
from os.path import isfile, join

folder = root = os.path.dirname(os.path.realpath(__file__))

def list_archetypes():
    files = [ f for f in listdir(folder) if isfile(join(folder,f)) ]
    
    files.pop(files.index('list.py'))
    files.pop(files.index('__init__.py'))

    names = []

    #print files

    for i in files:
        name = i.split('.')[0]
        if '_' in name:
            name = name.split('_')
            while True:
                try:
                    n = name.index('')
                    name.pop(n)
                except:
                    break
        name = ' '.join(name)
        names.append(name)
        time.sleep(0.1)
    names.sort()
    print names
            

if __name__ == '__main__':
    list_archetypes()
