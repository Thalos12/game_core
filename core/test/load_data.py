import os


def load(name):
    try:
        os.path.isfile(name)
    except:
        print "No profile found."
