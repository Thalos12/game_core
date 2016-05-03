# coding=utf-8
import sys
import os
import cStringIO
import profiledb
import wx
from archetypes import list_archetypes
from classes.player import Player
from GUI import gui
from classes.login_panel import LoginPanel


root = os.path.dirname(os.path.realpath(__file__))
sys.path.append(root)


# noinspection PyPep8Naming
class Game(wx.Frame):
    def __init__(self, options):
        super(Game, self).__init__(parent=None, title='Children of the Goddess', size=(600, 600),
                                   style=wx.MINIMIZE_BOX | wx.CLOSE_BOX)
        self.options = options
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.login = LoginPanel(self)
        self.sizer.Add(self.login, 1, wx.EXPAND | wx.ALL, 0)
        self.SetSizer(self.sizer)
        self.Center()
        self.Show()

    def main_menu(self, options):
        self.menu_sizer = wx.Sizer(wx.HORIZONTAL)
        self.sizer_l.Clear(True)
        self.panel_l.ClearBackground()
        self.panel_l.SetBackgroundColour(wx.Colour(230, 120, 100, 140))
        image_file = os.path.join(root, 'graphics', 'images', 'guerriero.jpg')
        data = open(image_file, "rb").read()
        stream = cStringIO.StringIO(data)
        bmp = wx.BitmapFromImage(wx.ImageFromStream(stream))
        bmp.SetWidth(self.panel_l.Size[0] - 20)
        bmp.SetHeight(self.panel_l.Size[1] - 20)
        bitmap = wx.StaticBitmap(self.panel_l, -1, bmp, (10, 10))
        self.sizer_l.Add(bitmap, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 10)

        self.sizer.Clear(True)

    def new_profile(self, evt):
        self.panel_new_profile = wx.Panel(self)
        self.sizer_new_profile = wx.BoxSizer(wx.VERTICAL)

        label1 = wx.StaticText(self.panel_new_profile, label='Write your name please.')
        player_name = wx.TextCtrl(self)
        label2 = wx.StaticText(self.panel_new_profile, label='Choose an archetype.')
        arch = list_archetypes.get_list()
        archetypes_listbox = wx.ListBox(self.panel_new_profile, choices=arch, style=wx.LB_SINGLE)
        ok = wx.Button(self.panel_new_profile, label='Ok')

        self.sizer_new_profile.AddMany([(label1, 0, wx.ALL, 5),
                                        (player_name, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT, 5),
                                        (label2, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT, 5),
                                        (archetypes_listbox, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT, 5),
                                        (ok, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT, 5)])
        self.panel_new_profile.SetSizer(self.sizer_new_profile)
        self.panel_new_profile.SetBackgroundColour(wx.Colour(255, 100, 100, 200))

        self.sizer.Clear(True)
        self.sizer.Add(self.panel_new_profile, 1, wx.EXPAND, 5)
        self.SetSizer(self.sizer)
        self.Layout()

    def ok(self, evt):
        name = self.profiles[self.profile_listbox.GetSelection()]
        stats = profiledb.load(name)
        try:
            self.player = Player(stats)
        except:
            gui.notification(None, 'Your profile cannot be loaded.')
            sys.exit()
        gui.notification(None, 'You are now ready to play!', caption="Loaded player profile")
        self.main_menu(self.options)

    def on_close(self, e):
        print "End."
        e.Skip()
        self.Destroy()

if __name__ == '__main__':
    sys.exit()
