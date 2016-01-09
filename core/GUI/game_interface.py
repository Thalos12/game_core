import os,sys
import wx
import profile


class Game(wx.Frame):
    def __init__(self, parent, title):
        super(Game, self).__init__(parent=parent, title=title ,size=(300,200),style=wx.MINIMIZE_BOX|wx.CLOSE_BOX)

        self.play_intro()

        self.profile_name = profile.ask_name(self)

        if self.profile_name in profile.get_names_list():
            self.initUI()
            self.Show(True)
        else:
            sys.exit()

    def initUI(self):
        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, '&About', "Info on this app")
        menubar = wx.MenuBar()
        menubar.Append(filemenu,'&File')
        self.Bind(wx.EVT_MENU,self.OnAbout,menuAbout)
        self.SetMenuBar(menubar)

        self.init_main_menu()

        self.SetMinSize((300,200))

    def init_main_menu(self):
        self.main_menu = wx.Panel(self)

        name_label = wx.StaticText(self.main_menu,id=wx.ID_ANY,label='Profile name:',style=wx.ALIGN_LEFT)
        name = wx.StaticText(self.main_menu,id=wx.ID_ANY,label=self.profile_name,style=wx.ALIGN_RIGHT)

        fgs = wx.FlexGridSizer(1,2,9,0)
        fgs.AddGrowableCol(0,1)
        fgs.AddGrowableCol(1,1)
        fgs.Add(name_label,1,wx.EXPAND|wx.LEFT|wx.TOP,10)
        fgs.Add(name,1,wx.EXPAND|wx.RIGHT|wx.TOP,10)

        self.main_menu.SetSizer(fgs)

    def OnAbout(self,e):
        dlg = wx.MessageDialog(self, "This is but a small app.","About this app.",wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def play_intro(self):
        pass

    def ask_name(self):
        ask = wx.TextEntryDialog(self,message='Name check.',caption='Cheking your name.',style=wx.OK,pos=(200,150))
        ask.ShowModal()
        name = ask.GetValue()
        ask.Destroy()
        return name


if __name__ == '__main__':
    app = wx.App(False)
    frame = Game(None, "Simple editor")
    app.MainLoop()

