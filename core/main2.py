import sys
import os
import logging
import time
import cStringIO
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
        super(Game, self).__init__(parent=None, title='Children of the Goddess', size=(600,400), style=wx.MINIMIZE_BOX|wx.CLOSE_BOX)

        names = profiledb.list_all()
        sorted(names, key=str.lower)
        names.insert(0,'Create new')

        name_index = gui.single_choice(None,"Load or create a profile.",names)
        if name_index!=None:
            name = names[name_index]
        else:
            gui.notification(None,"Nothing selected.")
            sys.exit()

        if name == 'Create new':
            name = gui.create_new(None)
            index = gui.single_choice(None,"Please select one of the archetypes.",list_archetypes.get_list())
            if index != None:
                archetype = list_archetypes.get_list()[index]
                profiledb.create(name,archetype)
            else:
                gui.notification(None,"No archetype selected.")
        else:
            gui.welcome_back(None,name)

        stats = profiledb.load(name)
        if stats == 'non-existent':
            gui.notification(None,'Your profile does not exist.')
            sys.exit()
        elif stats == 'corrupted':
            gui.notification(None,'Your data is corrupted, delete it and start over.')
            sys.exit()
        try:
            self.player = Player(stats)
        except:
            gui.notification(None,'Your profile cannot be loaded.')
            logging.error(('Your profile cannot be loaded. This happens when the player '
                           'class has been modified in such a way that your profile no '
                           'longer has the necessary requirements to be loaded. '
                           'Delete it and start over. We are sorry for the inconvenience.'))
            sys.exit()
        gui.notification(None,'You are now ready to play!',caption="Loaded player profile")

        logging.info("Running.")
        self.main_menu(options)

    def main_menu(self,options):
        self.menu_panel = wx.Panel(self)

        notebook = wx.Notebook(self.menu_panel)

        pg1 = wx.Panel(notebook)
        imageFile = os.path.join(root,'graphics','images','land.jpg')
        data = open(imageFile, "rb").read()
        stream = cStringIO.StringIO(data)
        bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))
        bmp.SetWidth(self.Size[0]-20)
        bmp.SetHeight(self.Size[1]-20)
        bitmap = wx.StaticBitmap(pg1, -1, bmp, (5, 5))
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        sizer2.Add(bitmap,0,wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,10)
        pg1.SetSizer(sizer2)

        pg2 = gui.stats_page(notebook,self.player,self.Size)

        notebook.AddPage(pg1,"Image")
        notebook.AddPage(pg2,"Stats")

        self.menu_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.menu_sizer.Add(notebook,1,wx.EXPAND)
        self.menu_panel.SetSizer(self.menu_sizer)


        self.Center()
        self.Show(True)

if __name__ == '__main__':
    sys.exit()
