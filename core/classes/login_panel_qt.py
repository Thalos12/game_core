# coding=utf-8
from PyQt5.QtWidgets import QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QListWidget, QPushButton
from core import profiledb


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
