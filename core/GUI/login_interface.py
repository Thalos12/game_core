# coding=utf-8
import os
import sys

import wx

import core.profiledb as profiledb


class LoginFrame(wx.Panel):
    def __init__(self,parent, size=(400,400), *args, **kwargs):
        super(LoginFrame, self).__init__(parent, *args, **kwargs)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)

        # generation of the left side of the frame
        self.l_panel = wx.Panel(self)
        self.profiles=profiledb.list_all()
        self.profile_listbox = wx.ListBox(self.l_panel, choices=self.profiles, style=wx.LB_SINGLE)
        self.profile_listbox.SetSelection(0)
        ok_btn = wx.Button(self.l_panel,label='Ok')
        quit_btn = wx.Button(self.l_panel,label='Quit')
        mid_sizer = wx.BoxSizer(wx.HORIZONTAL)
        mid_sizer.AddMany([(ok_btn,0,wx.LEFT|wx.RIGHT,5),
                           (quit_btn,0,wx.RIGHT,5)])
        new_btn = wx.Button(self.l_panel, label='Create new profile')
        l_sizer = wx.BoxSizer(wx.VERTICAL)
        l_sizer.AddMany([(self.profile_listbox, 1, wx.LEFT | wx.TOP | wx.RIGHT | wx.EXPAND, 5),
                         ((-1,10)),
                         (mid_sizer,0,wx.ALL|wx.ALIGN_CENTER_HORIZONTAL,5),
                         ((-1,15)),
                         (new_btn,0,wx.ALL|wx.ALIGN_CENTER_HORIZONTAL,5),
                         ((-1,20))])
        self.l_panel.SetSizer(l_sizer)
        self.l_panel.SetBackgroundColour(wx.Colour(48, 94, 232, 150))
        self.l_panel.Fit()

        # generation of the right side of the frame
        self.r_panel = wx.Panel(self)
        r_sizer = wx.BoxSizer(wx.VERTICAL)
        self.player_info = wx.StaticText(self.r_panel,label="")
        self.player_info.SetLabel(self.get_stats(self.r_panel, self.profiles[self.profile_listbox.GetSelection()]))
        del_btn = wx.Button(self.r_panel, label='Delete profile')
        r_sizer.AddMany([(self.player_info,1,wx.ALL|wx.EXPAND,5),
                         (del_btn,0,wx.LEFT|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL,5)])
        self.r_panel.SetSizer(r_sizer)
        self.r_panel.SetBackgroundColour(wx.Colour(255, 102, 0, 200))
        self.r_panel.Fit()

        # event handling
        self.profile_listbox.Bind(wx.EVT_LISTBOX, self.change_text)
        ok_btn.Bind(wx.EVT_BUTTON, self.ok)
        quit_btn.Bind(wx.EVT_BUTTON, self.quit)
        new_btn.Bind(wx.EVT_BUTTON, self.new_profile)
        del_btn.Bind(wx.EVT_BUTTON, self.delete_profile)

        self.sizer.AddMany([(self.l_panel,1,wx.EXPAND|wx.ALL,2),
                            ((-1,10)),
                            (self.r_panel,1,wx.EXPAND|wx.ALL,2)])
        self.Center()
        self.Show()


    def change_text(self,evt):
        self.player_info.SetLabel(self.get_stats(self.r_panel, profiledb.list_all()[self.profile_listbox.GetSelection()]))

    def delete_profile(self,evt):
        profile_name = self.profiles[self.profile_listbox.GetSelection()]
        profiledb.delete(profile_name)
        self.profiles=profiledb.list_all()
        self.profile_listbox = wx.ListBox(self.l_panel, choices=self.profiles, style=wx.LB_SINGLE)

    def get_stats(self,parent,name):
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
             "Skill: {}").format(stats['NAME'],stats['LEVEL'],stats['EXP'], stats['MONEY'],stats['VIT'],stats['STR'],
                             stats['RES'],stats['AGI'],stats['INT'],stats['WEAPON'],stats['ARMOR'],stats['SKILL'])
        return s

    def new_profile(self,evt):
        self.panel2 = wx.Panel(self)
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        label1 = wx.StaticText(self.panel2,label='Write your name please.')
        player_name = wx.TextCtrl(self)
        self.sizer2.AddMany([(label1,1,wx.ALL|wx.EXPAND,5),
                             (player_name,1,wx.LEFT|wx.BOTTOM|wx.RIGHT|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,5)])
        self.panel2.SetSizer(self.sizer2)
        self.panel2.SetBackgroundColour(wx.Colour(255,100,100,200))
        self.l_panel.Hide()
        self.r_panel.Hide()
        self.panel2.Fit()

    def ok(self,evt):
        name = self.profiles[self.profile_listbox.GetSelection()]
        stats = profiledb.load(name)
        self.stats = stats
        self.Close()
        self.MakeModal(False)