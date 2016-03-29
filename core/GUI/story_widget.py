import sys, os
import wx

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class StoryWidget(wx.Panel):
    def __init__(self, chapter, scene, parent, size=(200,100)):
        super(StoryWidget, self).__init__(parent=parent, size=size)
        self.scene = scene
        self.chapter=chapter
        self.text_area = wx.StaticText(self,style=wx.ALIGN_LEFT|wx.ST_ELLIPSIZE_END)
        self.sizer=wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.text_area,1,wx.EXPAND|wx.ALL,10)
        self.SetSizer(self.sizer)

    def display_text(self,):
        with open(os.path.join(root, 'text', self.chapter, str(self.scene) + '.txt')) as t:
            self.text = t.read()

        timer = wx.Timer
        s=''
        for i in self.text.split(' '):
            while not timer.Start(milliseconds=2000):
                pass
            self.text_area.SetLabel()

if __name__ == '__main__':
    app=wx.App(False)
    frame = wx.Frame(None,size=(300,300))
    s = StoryWidget('test',1,frame)
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    sizer.Add(s,1,wx.EXPAND)
    frame.SetSizer(sizer)
    frame.Show()
    app.MainLoop()