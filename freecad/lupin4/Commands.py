

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
        if FreeCAD.ActiveDocument is None:
            QtWidgets.QMessageBox.critical(FreeCADGui.getMainWindow(),"Error!", "mate, you need an active document in a project directory to proceed...")
            raise Exception("Stopping macro here")
        
        parameter = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/lupin4")
        print(f"parameter = {parameter}")
        print(f"downloadDirectory = {downloadDirectory}")
        print(f"type(parameter) = {type(parameter)}")
        if not parameter.getString(downloadDirectory, ""):
            QtWidgets.QMessageBox.critical(FreeCADGui.getMainWindow(),"Error!", "mate, I can't find any directories to download, you need to set them again!")
            #ask for a download path
            chosen = QtWidgets.QFileDialog.getExistingDirectory(FreeCADGui.getMainWindow(), "choose a folder mate", str( Path.cwd() / "Downloads"))
            FreeCAD.Console.PrintMessage(str(chosen) + "\n")

            parameter.SetString("downloadDirectory", str(chosen))

        
        """Run when the user clicks the toolbar button or menu item."""
        FreeCAD.Console.PrintMessage("Hello from the Minimal workbench!\n")
        FreeCAD.Console.PrintMessage("starting browser........................!\n")
        


        currentDirectory = os.path.dirname(os.path.abspath(__file__))
        
        FreeCAD.Console.PrintMessage(currentDirectory, "             currentdirectory\n")
        
        mainBrowserDirectory = str(currentDirectory + "/simplebrowser")
        
        FreeCAD.Console.PrintMessage(mainBrowserDirectory, "                               mainBrowserDirectory\n")
        
        mainBrowserPath = str(mainBrowserDirectory + "/main.py")
        
        FreeCAD.Console.PrintMessage(mainBrowserPath,"             mainPath\n")

        subprocess.Popen(["/usr/bin/python3", mainBrowserPath],cwd=mainBrowserDirectory)
        FreeCAD.Console.PrintMessage("\n")







FreeCADGui.addCommand("Minimal_Hello", HelloCommand())


