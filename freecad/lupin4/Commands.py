

import FreeCAD
import FreeCADGui
import sys
import os
import subprocess
from pathlib import Path
#from simplebrowser.main import runBrowser

try:
  from PySide6 import QtWebEngineWidgets, QtWidgets, QtCore, QtWebEngineCore
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
        FreeCAD.Console.PrintMessage("starting browser........................!\n")
        


        currentDirectory = os.path.dirname(os.path.abspath(__file__))
        
        FreeCAD.Console.PrintMessage(currentDirectory, "             currentdirectory\n")
        
        mainDirectory = str(currentDirectory / "simplebrowser")
        
        FreeCAD.Console.PrintMessage(mainDirectory, "                               mainDirectory\n")
        
        mainPath = str(currentDirectory / "simplebrowser" / "main.py")
        
        FreeCAD.Console.PrintMessage(mainPath,"             mainPath\n")

        subprocess.Popen(["/usr/bin/python3", mainPath],cwd=currentDirectory)
        FreeCAD.Console.PrintMessage("\n")







FreeCADGui.addCommand("Minimal_Hello", HelloCommand())


