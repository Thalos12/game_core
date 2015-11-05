import os

def update():
    print os.popen('git pull origin master').read()

update()
