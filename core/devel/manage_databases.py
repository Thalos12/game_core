import sys, os
import wx

class DatabaseManager(wx.Frame):
    def __init__(self):
        super(DatabaseManager, self).__init__(None,size=(400,400))
        root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        database_list = self.dblist(root)

        self.l_panel = wx.Panel(self)
        self.l_sizer = wx.BoxSizer(wx.VERTICAL)
        listbox = wx.ListBox(self.l_panel,choices=[f.split('/')[-1] for f in database_list],style=wx.LB_SINGLE)
        self.l_sizer.Add(listbox,1,wx.EXPAND|wx.ALL,5)

        self.r_panel = wx.Panel(self)
        self.r_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.AddMany([(self.l_panel,1,wx.EXPAND|wx.ALL,5),
                            (self.r_panel,1,wx.EXPAND|wx.ALL,5)])
        self.SetSizer(self.sizer)
        self.Fit()
        self.Show()

    def dblist(self,directory):
        dirlist = os.listdir(directory)
        s=list()
        for i in dirlist:
            p = os.path.join(directory,i)
            if os.path.isdir(p):
                f = self.dblist(p)
                if f != []:
                    for element in f:
                        s.append(element)
            elif i.split(os.pathsep)[-1].split('.')[-1] == 'db':
                s.append(p)
        return s


app = wx.App(False)
frame = DatabaseManager()
app.MainLoop()