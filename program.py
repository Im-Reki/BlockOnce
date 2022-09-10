import sys
import os
import webbrowser
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt5.QtGui import QFontDatabase, QIcon, QCursor
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUiType

# Warning Environment

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
os.environ["QT_SCALE_FACTOR"] = "1"

# ----------------------------------------------------------


Ui_MainWindow, QtBaseClass = loadUiType("template.ui")


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.filePath = ""
        # Icon
        self.setWindowIcon(QIcon("logo.ico"))
        # Fonts
        QFontDatabase.addApplicationFont(r".\fonts\SocialMedia.otf")
        QFontDatabase.addApplicationFont(r".\fonts\MyLogo.ttf")
        QFontDatabase.addApplicationFont(r".\fonts\Roboto-Medium.ttf")
        QFontDatabase.addApplicationFont(r".\fonts\Roboto-Italic.ttf")
        QFontDatabase.addApplicationFont(r".\fonts\Roboto-Regular.ttf")
        # Window Attributes
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.statusBar().setVisible(False)
        # Buttons
        self.btn_explorer.clicked.connect(self.explorerWindow)
        self.btn_start.clicked.connect(self.startButton)
        self.btn_github.clicked.connect(self.githubButton)
        self.btn_logo.clicked.connect(self.profileButton)
        self.btn_minimized.clicked.connect(self.minimizedButton)
        self.btn_close.clicked.connect(self.exitButton)
        self.btn_github.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logo.setCursor(QCursor(Qt.PointingHandCursor))
# Windows File Explorer Button

    def explorerWindow(self):
        filePath = QFileDialog.getOpenFileName(
            self, "Open File", "", "All Files (*)")
        self.filePath = filePath[0]
        self.lineEdit.setText(filePath[0])
# Start Button, executes a batch line.

    def startButton(self):
        if (len(self.filePath) > 0):
            cmd = "netsh advfirewall firewall add rule name=BlockOnce dir=out action=block program=\"" + \
                self.filePath.replace("/", "\\",) + "\" enable=yes"
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
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()
