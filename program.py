import tkinter as tk
from tkinter import filedialog
import sys
import os
import webbrowser
from PyQt5 import QtWidgets, uic, QtCore, QtGui


#----------------------------------------------------------

qtcreator_file  = "template.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)        
        self.filePath = ""
        # Icon
        self.setWindowIcon(QtGui.QIcon("logo.ico"))
        # Fonts
        QtGui.QFontDatabase.addApplicationFont (r".\fonts\SocialMedia.otf")
        QtGui.QFontDatabase.addApplicationFont (r".\fonts\MyLogo.ttf")
        QtGui.QFontDatabase.addApplicationFont (r".\fonts\Roboto-Medium.ttf")
        QtGui.QFontDatabase.addApplicationFont (r".\fonts\Roboto-Italic.ttf")
        QtGui.QFontDatabase.addApplicationFont (r".\fonts\Roboto-Reglular.ttf")
        # Window Attributes
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.statusBar().setVisible(False)
        # Effects
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_7.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_8.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_9.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        # Buttons
        self.btn_explorer.clicked.connect(self.explorerWindow)
        self.btn_start.clicked.connect(self.startButton)
        self.btn_github.clicked.connect(self.githubButton)
        self.btn_logo.clicked.connect(self.profileButton)
        self.btn_minimized.clicked.connect(self.minimizedButton)
        self.btn_close.clicked.connect(self.exitButton)
# Windows File Explorer Button
    def explorerWindow(self):
        root = tk.Tk()
        root.withdraw()
        filePath = filedialog.askopenfilename()
        self.filePath = filePath
        self.lineEdit.setText(filePath)
# Start Button, executes a batch line.
    def startButton(self):
        if (len(self.filePath) > 0):
            cmd = "netsh advfirewall firewall add rule name=BlockOnce dir=out action=block program=\"" + self.filePath.replace("/", "\\",) + "\" enable=yes"
            os.system(cmd)
# Link to my Github profile
    def profileButton(self):
        webbrowser.open("https://github.com/Im-Reki")
# Link to the Repository
    def githubButton(self):
        webbrowser.open("https://github.com/Im-Reki/BlockOnce")
# Minimize Button
    def minimizedButton(self):
        self.showMinimized()
# Exit Button
    def exitButton(self):
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())