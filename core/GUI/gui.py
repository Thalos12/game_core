# coding=utf-8
import wx
import os

def ask_name(parent):
    ask = wx.TextEntryDialog(parent, message='Checking your name.', caption='Name check', style=wx.OK)
    ask.Center()
    ask.ShowModal()
    name = ask.GetValue()
    ask.Destroy()
    return name

def create_new(parent):
    dialog = wx.TextEntryDialog(parent, message='You need to enter a nickname, please.', caption='New profile', style=wx.OK)
    dialog.Center()
    dialog.ShowModal()
    name = dialog.GetValue()
    dialog.Destroy()
    return name

def notification(parent,message,caption='Notification'):
    message = wx.MessageDialog(parent, message=message, caption=caption, style=wx.OK|wx.ICON_INFORMATION)
    message.Center()
    message.ShowModal()
    message.Destroy()

def show_player_info(parent,stats):
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
    notification(parent,s,"Your stats")

def show_weapon_info(parent,weapon):
    s = ("Name: {}\n"
         "Kind: {}\n"
         "Description: {}\n"
         "Pierce damage modifier: {}\n"
         "Slash damage modifier: {}\n"
         "Impact damage modifier: {}\n"
         "Ranged damage modifier: {}\n"
         "Magic damage modifier: {}\n").format(weapon.NAME, weapon.KIND, weapon.DESCRIPTION,
                                               weapon.PIERCE_DAMAGE_MODIFIER, weapon.SLASH_DAMAGE_MODIFIER,
                                               weapon.IMPACT_DAMAGE_MODIFIER, weapon.RANGED_DAMAGE_MODIFIER,
                                               weapon.MAGIC_DAMAGE_MODIFIER)
    notification(parent,s,"Your weapon's stats")

def show_armor_info(parent,armor):
    s = ("Name: {}\n"
         "Kind: {}\n"
         "Description: {}\n"
         "Pierce damage reduce: {}\n"
         "Slash damage reduce: {}\n"
         "Impact damage reduce: {}\n"
         "Ranged damage reduce: {}\n"
         "Magic damage reduce: {}\n").format(armor.NAME, armor.KIND, armor.DESCRIPTION,
                                               armor.PIERCE_DAMAGE_REDUCE, armor.SLASH_DAMAGE_REDUCE,
                                               armor.IMPACT_DAMAGE_REDUCE, armor.RANGED_DAMAGE_REDUCE,
                                               armor.MAGIC_DAMAGE_REDUCE)
    notification(parent,s,"Your armor's stats")

def show_skill_info(parent,skill):
    s = ("Name: {}\n"
         "Description: {}\n"
         "Effect: {}\n").format(skill.NAME, skill.DESCRIPTION, skill.EFFECT)
    notification(parent,s,"Your skill's stats")

def single_choice(parent,message,choices):
    sc = wx.SingleChoiceDialog(parent, message=message, caption='Choose one', choices=choices)
    sc.Center()
    if sc.ShowModal() == wx.ID_OK:
        choice = sc.GetSelection()
    else:
        choice = None
    sc.Destroy()
    return choice

def stats_page(parent,player,frame_size):
    page = wx.Panel(parent)

    sizer1 = wx.BoxSizer(wx.VERTICAL)
    sizer2 = wx.BoxSizer(wx.VERTICAL)
    for element in player.stats.keys():
        label1 = wx.StaticText(page,label=element.lower())
        label2 = wx.StaticText(page,label=str(player.stats[element]))
        sizer1.Add(label1,0,wx.ALL,10)
        sizer2.Add(label2,0,wx.ALL,10)

    page_sizer = wx.BoxSizer(wx.HORIZONTAL)
    page_sizer.AddMany([(sizer1,0,wx.ALL,10),
                        (sizer2,0,wx.ALL,10)])
    page.SetSizer(page_sizer)
    return page

def welcome_back(parent,name):
    welcome = wx.MessageDialog(parent, message='Welcome back '+name+'!', caption='Message', style=wx.OK|wx.ICON_INFORMATION)
    welcome.Center()
    welcome.ShowModal()
    welcome.Destroy()

def yes_no(parent,message):
    yn = wx.MessageDialog(parent, message=message, caption="Action required", style=wx.YES_NO|wx.YES_DEFAULT|wx.ICON_INFORMATION|wx.CENTRE)
    yn.Center()
    ans = yn.ShowModal()
    yn.Destroy()
    if ans == wx.ID_YES:
        return 'y'
    else:
        return 'n'