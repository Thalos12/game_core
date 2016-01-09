import os,time
from os import listdir
from os.path import isfile, join

folder = root = os.path.dirname(os.path.realpath(__file__))

def get_list():
    # listing files
    files = [ f for f in listdir(folder) if isfile(join(folder,f)) ]
    # removing what is not needed
    files.pop(files.index('list_archetypes.pyc'))
    files.pop(files.index('__init__.pyc'))

    names = []
    for i in files:
        if i.split('.')[-1] != 'py':
            n = i.split('.')[0]
            n = n.split('_')
            name = ' '.join(n)
            names.append(name)
    return names

if __name__ == '__main__':
    get_list()
