import os
import FreeCADGui

_ADDON_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ICON = os.path.join(_ADDON_ROOT, "Resources", "Icons", "Logo.svg")


class lupin4Workbench(FreeCADGui.Workbench):


    MenuText = "Lupin4"
    ToolTip = "An importer for FreeCAD, find any files you\'d like in Misumi, McMaster, and GrabCAD."
    Icon = _ICON

    def Initialize(self):
        """Run once, the first time the user activates this workbench."""
        # Importing Commands has the side effect of calling
        # FreeCADGui.addCommand("Minimal_Hello", ...), which registers the
        # command by name so we can reference it below.
        from . import Commands

        self.appendToolbar("Lupin4", ["OpenImporter","Initialize","ImportEverything"])
        self.appendMenu("Lupin4", ["OpenImporter","Initialize","ImportEverything"])

    def GetClassName(self):
        """Required for Python workbenches. Must return this *exact* string, DO NOT MODIFY."""
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(lupin4Workbench())
