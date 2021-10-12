import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        backbtn = QAction('back', self)
        backbtn.triggered.connect(self.browser.back)
        navbar.addAction(backbtn)
        
        forwardbtn = QAction('forward', self)
        forwardbtn.triggered.connect(self.browser.forward)
        navbar.addAction(forwardbtn)
        
        reloadbtn = QAction('reload', self)
        reloadbtn.triggered.connect(self.browser.reload)
        navbar.addAction(reloadbtn)
        
        homebtn = QAction('home', self)
        homebtn.triggered.connect(self.navigate_home)
        navbar.addAction(homebtn)
        
        devbtn = QAction('Developer', self)
        devbtn.triggered.connect(self.navigate_developer)
        navbar.addAction(devbtn)
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
        
    def navigate_developer(self):
        self.browser.setUrl(QUrl('https://elijahknsubuga.netlify.app/'))
        
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        
    def update_url(self, q):
        self.url_bar.setText(q.toString())
        
app = QApplication(sys.argv)
QApplication.setApplicationName('by elijah')
window = MainWindow()
app.exec_()
