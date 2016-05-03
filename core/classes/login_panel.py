# coding=utf-8
import sys
import wx
from core.classes.player import Player
from core.archetypes import list_archetypes
from core import profiledb
from core.profiledb import get_stats
from core.GUI import gui


class LoginPanel(wx.Panel):
    def __init__(self, parent):
        self.parent = parent
        super(LoginPanel, self).__init__(parent=self.parent)
        # panel sizer
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # generation of the left side of the frame
        self.panel_l = wx.Panel(parent)
        self.profiles = profiledb.list_all()
        self.profile_listbox = wx.ListBox(self.panel_l, choices=self.profiles, style=wx.LB_SINGLE)
        self.profile_listbox.SetSelection(0)
        btn_ok = wx.Button(self.panel_l, label='Ok')
        btn_new = wx.Button(self.panel_l, label='Create new profile')
        self.sizer_l = wx.BoxSizer(wx.VERTICAL)
        self.sizer_l.AddMany([(self.profile_listbox, 1, wx.LEFT | wx.TOP | wx.RIGHT | wx.EXPAND, 5),
                              ((-1, 100)),
                              (btn_ok, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5),
                              ((-1, 15)),
                              (btn_new, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5),
                              ((-1, 20))])
        self.panel_l.SetSizer(self.sizer_l)
        self.panel_l.SetBackgroundColour(wx.Colour(48, 94, 232, 150))
        # self.panel_l.Fit()

        # generation of the right side of the frame
        self.panel_r = wx.Panel(parent)
        self.sizer_r = wx.BoxSizer(wx.VERTICAL)
        self.player_info = wx.StaticText(self.panel_r, label="")
        self.player_info.SetLabel(get_stats(self.panel_r,
                                            self.profiles[self.profile_listbox.GetSelection()]))
        btn_del = wx.Button(self.panel_r, label='Delete profile')
        self.sizer_r.AddMany([(self.player_info, 1, wx.ALL | wx.EXPAND, 5),
                              ((-1, 100)),
                              (btn_del, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL, 5),
                              ((-1, 20))])
        self.panel_r.SetSizer(self.sizer_r)
        self.panel_r.SetBackgroundColour(wx.Colour(255, 102, 0, 200))
        # self.panel_r.Fit()

        # event handling
        self.profile_listbox.Bind(wx.EVT_LISTBOX, self.change_text)
        btn_ok.Bind(wx.EVT_BUTTON, self.on_ok)
        btn_new.Bind(wx.EVT_BUTTON, self.new_profile)
        btn_del.Bind(wx.EVT_BUTTON, self.delete_profile)

        # adding to frame sizer
        self.sizer.AddMany([(self.panel_l, 1, wx.EXPAND | wx.ALL, 2),
                            ((-1, 10)),
                            (self.panel_r, 1, wx.EXPAND | wx.ALL, 2)])
        self.SetSizer(self.sizer)

    def change_text(self, evt):
        self.player_info.SetLabel(
            get_stats(self.panel_r, profiledb.list_all()[self.profile_listbox.GetSelection()]))

    def delete_profile(self, evt):
        profile_name = self.profiles[self.profile_listbox.GetSelection()]
        profiledb.delete(profile_name)
        self.profiles = profiledb.list_all()
        self.profile_listbox = wx.ListBox(self.panel_l, choices=self.profiles, style=wx.LB_SINGLE)

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

    def on_ok(self, evt):
        name = self.profiles[self.profile_listbox.GetSelection()]
        stats = profiledb.load(name)
        try:
            self.player = Player(stats)
        except:
            gui.notification(None, 'Your profile cannot be loaded.')
            sys.exit()
        gui.notification(None, 'You are now ready to play!', caption="Loaded player profile")
        self.parent.main_menu(self.options)
