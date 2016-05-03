# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QAction, QApplication, QToolBar, QMessageBox, QHBoxLayout,
                             QPushButton, QVBoxLayout, QDesktopWidget, QSizePolicy, QListWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from core import profiledb


class MainMenu(QMainWindow):
    def __init__(self, parent=None, options={}):
        super(MainMenu, self).__init__(parent)
        self.initUI()
        self.setToolTip('Main window.')

    def initUI(self):
        # definisco le azioni
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

        # aggiungo il widget centrale
        self.setCentralWidget(LoginWindow(self))

        # cambio posizione e dimensioni della finestra e ne definisco il titiolo infine la faccio apparire
        self.resize(600, 400)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowTitle('Main window')
        self.show()

        # imposto la statusbar per scrivere che l'app è pronta
        self.statusBar().showMessage('Ready')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.parent = parent
        layout = QHBoxLayout()
        layout.addWidget(self.left_widget())
        layout.addWidget(self.right_widget())
        self.setLayout(layout)
        self.setToolTip('Child widget.')

    def left_widget(self):
        listview = QListWidget(self)
        listview.addItems([i for i in profiledb.list_all()])
        listview.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        btn = QPushButton('left widget', self)
        btn.setToolTip('Button of the <b>left widget</b>.')
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QVBoxLayout(self)
        layout.addWidget(listview)
        layout.addWidget(btn)
        layout.addStretch(1)

        widg = QWidget(self)
        widg.setLayout(layout)
        widg.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        
        return widg

    def right_widget(self):
        btn = QPushButton('right widget', self)
        btn.setToolTip('Button of the <b>right widget</b>.')
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QVBoxLayout(self)
        layout.addWidget(btn)
        layout.addStretch(1)

        widg = QWidget(self)
        widg.setLayout(layout)

        return widg


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainMenu()
    sys.exit(app.exec_())
