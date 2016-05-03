import os
import wx
# Under this line place the temporary imports

_root = os.path.dirname(os.path.realpath(__file__))


class TestFrame(wx.Frame):

    def __init__(self):
        super(TestFrame, self).__init__(parent=None, title='Test Frame', size=(600, 600),
                                        style=wx.MINIMIZE_BOX | wx.CLOSE_BOX)
        # self.options = options
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self.sizer)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Center()
        self.Show()

    def on_close(self, e):
        print "End."
        e.Skip()
        self.Destroy()

    # Under this line place the temporary functions


# Under this line place the temporary classes
class Lifebar(wx.Panel):
    def __init__(self, parent):
        super(Lifebar, self).__init__(parent=parent)
        self.sizer = wx.Sizer(wx.VERTICAL)


if __name__ == '__main__':
    app = wx.App()
    frame = TestFrame()
    app.mainloop()
