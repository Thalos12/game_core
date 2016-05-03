# coding=utf-8
import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QAction,
                             QDesktopWidget, QMessageBox, QToolBar, QStackedWidget)
from PyQt5.QtCore import Qt
import profiledb
from archetypes import list_archetypes
from classes.player import Player
from GUI import gui
from classes.login_panel_qt import LoginWindow


root = os.path.dirname(os.path.realpath(__file__))
sys.path.append(root)


# noinspection PyPep8Naming
class Game(QMainWindow):
    def __init__(self, options):
        super(Game, self).__init__(parent=None)
        self.options = options
        self.initUI()
        self.setCentralWidget(LoginWindow)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def initUI(self):
        self.setWindowTitle("Children of the Goddess")

        # definisco l'azione ala chiusura
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        # creo la barra dei menu e aggiungo i menu
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # creo la toolbar
        toolbar = QToolBar()
        toolbar.addAction(exitAction)
        self.addToolBar(Qt.RightToolBarArea, toolbar)  # toolbar di default sul lato destro della finestra

        # cambio posizione e dimensioni della finestra e ne definisco il titiolo infine la faccio apparire
        self.resize(600, 400)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowTitle('Main window')
        self.show()

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
