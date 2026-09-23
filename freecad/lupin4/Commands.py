

import FreeCAD
import FreeCADGui
import sys
import os
import subprocess
import ImportGui
from pathlib import Path
import threading
#from simplebrowser.main import runBrowser

try:
  from PySide6 import QtWebEngineWidgets, QtWidgets, QtCore, QtWebEngineCore
except ImportError:
  raise Exception("Missing package. Please install: python3-pyside2.qtwebenginewidgets.")


def runfunction():
    continue





class OpenImporter:
    def GetResources(self):
        return {
            "MenuText": "OpenImporter",
            "ToolTip": "Opens the importer, have fun with \'em",
            # "Pixmap":  "hello.svg",  # filename on the registered icon path
        }

    def IsActive(self):
        return True

    def Activated(self):
        if FreeCAD.ActiveDocument is None:
            QtWidgets.QMessageBox.critical(FreeCADGui.getMainWindow(),"Error!", "mate, you need an active document in a project directory to proceed...")
            return None
        

        params = FreeCAD.ParamGet("User parameter:BaseApp")
        parameter = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/lupin4")
        FreeCAD.Console.PrintMessage(f"parameter = {parameter}")
        FreeCAD.Console.PrintMessage(f"type(parameter) = {type(parameter)}")
        downloadDirectory = parameter.GetString("downloadDirectory", "")
        FreeCAD.Console.PrintMessage(str(downloadDirectory))
        
        """Run when the user clicks the toolbar button or menu item."""
        FreeCAD.Console.PrintMessage("Hello from the Minimal workbench!\n")
        FreeCAD.Console.PrintMessage("starting browser........................!\n")
        

        currentDirectory = os.path.dirname(os.path.abspath(__file__))

        
        mainBrowserDirectory = str(currentDirectory + "/simplebrowser")
        FreeCAD.Console.PrintMessage(mainBrowserDirectory, "                               mainBrowserDirectory\n")
        
        mainBrowserPath = str(mainBrowserDirectory + "/main.py") 
        FreeCAD.Console.PrintMessage(mainBrowserPath,"             mainPath\n")



        env = os.environ.copy()
        env['downloadPath'] = str(downloadDirectory)

        process = subprocess.Popen(["/usr/bin/python3", mainBrowserPath], env=env,cwd=mainBrowserDirectory,stdout=subprocess.PIPE,text=True)

        for line in process.stdout:
            filename = line.strip() # Process each line as it comes
            Free
            ImportGui.insert(downloadDirectory, filename)
        process.wait()  # Wait for it to finish
        FreeCAD.Console.PrintMessage("\n")

        




class Initialize:
    def GetResources(self):
        return {
            "MenuText": "Initialize",
            "ToolTip": "Set the directory, for your project",
            # "Pixmap":  "hello.svg",  # filename on the registered icon path
        }

    def IsActive(self):
        """Return True whenever the command should be enabled."""
        return True

    def Activated(self):
        if FreeCAD.ActiveDocument is None:
            QtWidgets.QMessageBox.critical(FreeCADGui.getMainWindow(),"Error!", "mate, you need an active document in a project directory to proceed...")
            return None
        

        params = FreeCAD.ParamGet("User parameter:BaseApp")
        parameter = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/lupin4")
        FreeCAD.Console.PrintMessage(f"parameter = {parameter}")
        FreeCAD.Console.PrintMessage(f"type(parameter) = {type(parameter)}")
        QtWidgets.QMessageBox.critical(FreeCADGui.getMainWindow(),"Error!", "mate, I can't find any directories to download, you need to set them again!")
        chosen = QtWidgets.QFileDialog.getExistingDirectory(FreeCADGui.getMainWindow(), "choose a folder mate", str( Path.cwd() / "Downloads"))
        #ask for a download path
        FreeCAD.Console.PrintMessage(str(chosen) + "\n")
        parameter.SetString("downloadDirectory", str(chosen))







FreeCADGui.addCommand("OpenImporter", OpenImporter())
FreeCADGui.addCommand("Initialize", Initialize())



