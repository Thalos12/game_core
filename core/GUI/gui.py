import wx

def ask_name(parent):
    ask = wx.TextEntryDialog(parent, message='Checking your name.', caption='Name check', style=wx.OK)
    ask.Center()
    ask.ShowModal()
    name = ask.GetValue()
    ask.Destroy()
    return name

def create_new(parent):
    dialog = wx.TextEntryDialog(parent, message='You need to create a new profile.\nEnter a nickname, please.', caption='New profile', style=wx.OK)
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

def single_choice(parent,message,choices):
    sc = wx.SingleChoiceDialog(parent, message=message, caption='Choose one', choices=choices)
    sc.Center()
    if sc.ShowModal() == wx.ID_OK:
        choice = sc.GetSelection()
    else:
        choice = None
    sc.Destroy()
    return choice

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