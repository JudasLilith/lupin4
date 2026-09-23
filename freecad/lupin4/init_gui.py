# SPDX-License-Identifier: CC0-1.0
# SPDX-FileNotice: Part of the Addon Academy "Minimal Workbench" demo.

"""FreeCAD startup hook: defines and registers the Minimal Workbench."""

import os

import FreeCADGui

# This file is at <addon-root>/freecad/MinimalWorkbench/init_gui.py, so the
# addon root is three directories up.
_ADDON_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ICON = os.path.join(_ADDON_ROOT, "Resources", "Icons", "Logo.svg")


class lupin4Workbench(FreeCADGui.Workbench):


    MenuText = "Lupin4"
    ToolTip = "An importer for FreeCAD."
    Icon = _ICON

    def Initialize(self):
        """Run once, the first time the user activates this workbench."""
        # Importing Commands has the side effect of calling
        # FreeCADGui.addCommand("Minimal_Hello", ...), which registers the
        # command by name so we can reference it below.
        from . import Commands  # noqa: F401

        self.appendToolbar("Lupin4", ["OpenImporter","Initialize"])
        self.appendMenu("Lupin4", ["OpenImporter","Initialize"])

    def GetClassName(self):
        """Required for Python workbenches. Must return this *exact* string, DO NOT MODIFY."""
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(lupin4Workbench())
