

import FreeCAD
import FreeCADGui
import os

from PySide import QtCore
from PySide import QtWidgets



import webbrowser
try:
  from PySide import QtWebEngineWidgets
except ImportError:
  raise Exception("Missing package. Please install: python3-pyside2.qtwebenginewidgets.")








class HelloCommand:
    """A one-line command that prints a message to the Report view."""

    def GetResources(self):
        return {
            "MenuText": "Hello",
            "ToolTip": "Print a hello message to the Report view.",
            # "Pixmap":  "hello.svg",  # filename on the registered icon path
        }

    def IsActive(self):
        """Return True whenever the command should be enabled."""
        return True

    def Activated(self):
        """Run when the user clicks the toolbar button or menu item."""
        FreeCAD.Console.PrintMessage("Hello from the Minimal workbench!\n")
        webbrowser.open("https://www.mcmaster.com/")


class Downloader:
    def __init___(self):
        self.downloadItem = QWebEngineCore.QWebEngineDownloadItem #this is the class?

    def download(self,download):
        downloadDirectory = os.path.expandUser("~/Downloads")

        filename = download.suggestedFileName()

        save_path




class Browser:
    _instance = None

    def __init__(self):

        self.webView = QtWebEngineWidgets.QWebEngineView()
        self.webView.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)



    def GetResources(self):
        return {
            "MenuText": "Browser",
            "ToolTip": "Open browser window",
        }

    def IsActive(self):
        return True

    def Activated(self):
        self.webView.load(QtCore.QUrl("https://www.mcmaster.com/"))
        self.webView.show()


    def getBrowser(self):
        return self.webView

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = Browser()
        return cls._instance





FreeCADGui.addCommand("Minimal_Hello", HelloCommand())


FreeCADGui.addCommand("Browser", Browser.getInstance())

