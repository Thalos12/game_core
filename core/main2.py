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
                archetype = list_archetypes.get_list()[index]
            else:
                sys.exit()
            profiledb.create(name,archetype)

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

        b1 = wx.Button(self.menu_panel,label='Player info')
        b1.Bind(wx.EVT_BUTTON, self.player.info)
        b2 = wx.Button(self.menu_panel,label='Weapon info')
        b2.Bind(wx.EVT_BUTTON, self.player.weapon.info)
        b3 = wx.Button(self.menu_panel,label='Armor info')
        b3.Bind(wx.EVT_BUTTON, self.player.armor.info)
        b4 = wx.Button(self.menu_panel,label='Skill info')
        b4.Bind(wx.EVT_BUTTON, self.player.skill.info)
        sizer1 = wx.BoxSizer(wx.VERTICAL)
        sizer1.AddMany([(b1,0,wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,10),
                       (b2,0,wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,10),
                       (b3,0,wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,10),
                       (b4,0,wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,10)])

        imageFile = os.path.join(root,'graphics','images','land.jpg')
        data = open(imageFile, "rb").read()
        stream = cStringIO.StringIO(data)
        bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))
        bmp.SetWidth(bmp.GetWidth()/10)
        bmp.SetHeight(bmp.GetHeight()/10)
        bitmap = wx.StaticBitmap(self.menu_panel, -1, bmp, (5, 5))
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        sizer2.Add(bitmap,0,wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,10)

        self.menu_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.menu_sizer.AddMany([(sizer2,0,wx.ALL|wx.EXPAND,10),
                                 (sizer1,0,wx.ALL|wx.EXPAND,10)])
        self.menu_panel.SetSizer(self.menu_sizer)
        self.menu_panel.Fit()


        self.Center()
        self.Fit()
        self.Show(True)

if __name__ == '__main__':
    sys.exit()
