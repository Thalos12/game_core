# coding=utf-8
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


root = os.path.dirname(os.path.realpath(__file__))
sys.path.append(root)


# noinspection PyPep8Naming
class Game(wx.Frame):
    def __init__(self, options):
        super(Game, self).__init__(parent=None, title='Children of the Goddess', size=(600,600), style=wx.MINIMIZE_BOX|wx.CLOSE_BOX)
        self.options = options
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.login()
        self.Center()
        self.Show()

    def login(self):
        # generation of the left side of the frame
        self.panel_l = wx.Panel(self)
        self.profiles = profiledb.list_all()
        self.profile_listbox = wx.ListBox(self.panel_l, choices=self.profiles, style=wx.LB_SINGLE)
        self.profile_listbox.SetSelection(0)
        btn_ok = wx.Button(self.panel_l, label='Ok')
        btn_new = wx.Button(self.panel_l, label='Create new profile')
        sizer_l = wx.BoxSizer(wx.VERTICAL)
        sizer_l.AddMany([(self.profile_listbox, 1, wx.LEFT | wx.TOP | wx.RIGHT | wx.EXPAND, 5),
                         ((-1, 10)),
                         (btn_ok, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5),
                         ((-1, 15)),
                         (btn_new, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5),
                         ((-1, 20))])
        self.panel_l.SetSizer(sizer_l)
        self.panel_l.SetBackgroundColour(wx.Colour(48, 94, 232, 150))
        self.panel_l.Fit()
        # generation of the right side of the frame
        self.panel_r = wx.Panel(self)
        sizer_r = wx.BoxSizer(wx.VERTICAL)
        self.player_info = wx.StaticText(self.panel_r, label="")
        self.player_info.SetLabel(self.get_stats(self.panel_r, self.profiles[self.profile_listbox.GetSelection()]))
        btn_del = wx.Button(self.panel_r, label='Delete profile')
        sizer_r.AddMany([(self.player_info, 1, wx.ALL | wx.EXPAND, 5),
                         (btn_del, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL, 5)])
        self.panel_r.SetSizer(sizer_r)
        self.panel_r.SetBackgroundColour(wx.Colour(255, 102, 0, 200))
        self.panel_r.Fit()
        # event handling
        self.profile_listbox.Bind(wx.EVT_LISTBOX, self.change_text)
        btn_ok.Bind(wx.EVT_BUTTON, self.ok)
        btn_new.Bind(wx.EVT_BUTTON, self.new_profile)
        btn_del.Bind(wx.EVT_BUTTON, self.delete_profile)
        # adding to frame sizer
        self.sizer.AddMany([(self.panel_l, 1, wx.EXPAND | wx.ALL, 2),
                            ((-1, 10)),
                            (self.panel_r, 1, wx.EXPAND | wx.ALL, 2)])

    def change_text(self, evt):
        self.player_info.SetLabel(
            self.get_stats(self.panel_r, profiledb.list_all()[self.profile_listbox.GetSelection()]))

    def delete_profile(self, evt):
        profile_name = self.profiles[self.profile_listbox.GetSelection()]
        profiledb.delete(profile_name)
        self.profiles = profiledb.list_all()
        self.profile_listbox = wx.ListBox(self.panel_l, choices=self.profiles, style=wx.LB_SINGLE)

    def get_stats(self, parent, name):
        stats = profiledb.load(name)
        s = ("Name: {}\n"
             "Level: {}\n"
             "Exp: {}\n"
             "Money: {}\n"
             "Vitality: {}\n"
             "Strength: {}\n"
             "Resistance: {}\n"
             "Agility: {}\n"
             "Intelligence: {}\n"
             "Weapon: {}\n"
             "Armor: {}\n"
             "Skill: {}").format(stats['NAME'], stats['LEVEL'], stats['EXP'], stats['MONEY'], stats['VIT'],
                                 stats['STR'],
                                 stats['RES'], stats['AGI'], stats['INT'], stats['WEAPON'], stats['ARMOR'],
                                 stats['SKILL'])
        return s

    def new_profile(self, evt):
        self.panel2 = wx.Panel(self)
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        label1 = wx.StaticText(self.panel2, label='Write your name please.')
        player_name = wx.TextCtrl(self)
        self.sizer2.AddMany([(label1, 1, wx.ALL | wx.EXPAND, 5),
                             (player_name, 1,
                              wx.LEFT | wx.BOTTOM | wx.RIGHT | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
                              5)])
        self.panel2.SetSizer(self.sizer2)
        self.panel2.SetBackgroundColour(wx.Colour(255, 100, 100, 200))
        self.panel_l.Hide()
        self.panel_r.Hide()
        self.panel2.Fit()

    def ok(self, evt):
        name = self.profiles[self.profile_listbox.GetSelection()]
        stats = profiledb.load(name)
        try:
            self.player = Player(stats)
        except:
            gui.notification(None, 'Your profile cannot be loaded.')
            logging.error(('Your profile cannot be loaded. This happens when the player '
                           'class has been modified in such a way that your profile no '
                           'longer has the necessary requirements to be loaded. '
                           'Delete it and start over. We are sorry for the inconvenience.'))
            sys.exit()
        gui.notification(None, 'You are now ready to play!', caption="Loaded player profile")
        logging.info("Running.")

        self.sizer.DeleteWindows()

        self.main_menu(self.options)

    def main_menu(self, options):
        #self.sizer = wx.BoxSizer(wx.VERTICAL)
        #self.SetSizer(self.sizer)
        self.menu_panel = wx.Panel(self)

        notebook = wx.Notebook(self.menu_panel)

        pg1 = wx.Panel(notebook)
        imageFile = os.path.join(root, 'graphics', 'images', 'land.jpg')
        data = open(imageFile, "rb").read()
        stream = cStringIO.StringIO(data)
        bmp = wx.BitmapFromImage(wx.ImageFromStream(stream))
        bmp.SetWidth(self.Size[0] - 20)
        bmp.SetHeight(self.Size[1] - 20)
        bitmap = wx.StaticBitmap(pg1, -1, bmp, (5, 5))
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        sizer2.Add(bitmap, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)
        pg1.SetSizer(sizer2)

        pg2 = gui.stats_page(notebook, self.player, self.Size)

        notebook.AddPage(pg1, "Image")
        notebook.AddPage(pg2, "Stats")

        self.menu_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.menu_sizer.Add(notebook, 1, wx.EXPAND)
        self.menu_panel.SetSizer(self.menu_sizer)

        self.sizer.Add(self.menu_panel,0,wx.ALL|wx.EXPAND,5)

        self.sizer.Layout()
        self.Center()
        self.Show(True)

    def on_close(self,e):
        print "End."
        e.Skip()
        self.Destroy()

if __name__ == '__main__':
    sys.exit()
