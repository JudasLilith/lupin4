![lupin image](./lupinNormalinverted.png)

<!-- Or embed SVG directly -->

# lupin4

A importing addon for FreeCAD

- Built on PyQt, FreeCAD, and the simplebrowser Example from Qt framework

### Introduction

- I recently have been trying out FreeCAD, and one of the hardest and tedious j\*bs I had was to import
  everything from GrabCAD and paste them down to the project directory. And, I thought maybe I'd learn some of the Qt framework due to its
  high usage in the CAD industry. So, I decided to slim out the process into 3 steps: initialize where you'd like the files to be saved, which is stored in the FreeCAD.config file; open up a dedicated PyQt browser to save all the files, and then import all of the saved files onto the current working document.

### Installation

- Installation can be done with the [FreeCAD Addons Manager](https://github.com/FreeCAD/AddonManager).

1. Type up: lupin4

2. install the program onto your pc, reload FreeCAD.
3. there are 3 main buttons: The OpenImporter, Initialize, and ImportEverything.
   ![list](./images/swappy-20260927-210008.png)

> [!CAUTION]
> be sure to have a working file, or else the first step wouldn't work.
> ![list](./images/swappy-20260927-210417.png)

1. set up a file that you would be comfortable for the program to store the imported files in.
   ![list](./images/swappy-20260927-210503.png)

1) after setting up, open up the OpenImporter, where there would be multiple tabs of GrabCAD, McMaster, and Misumi.
   ![list](./images/swappy-20260927-210601.png)

1. Make an account(Dw, all the login info is stored) and download the files as you would from a normal browser.
   ![list](./images/swappy-20260927-210612.png)

1) after downloading everything, press the ImportEverything button to load all the downloaded models onto your working file. Enjoy!

![list](./images/swappy-20260927-212855.png)

##### Inspired by/Based on

- [simplebrowser](https://doc.qt.io/qt-6/qtwebengine-webenginewidgets-simplebrowser-example.html)
- [djshaw01's custom addon](https://github.com/djshaw01/FreeCAD-McMasterCarr)
