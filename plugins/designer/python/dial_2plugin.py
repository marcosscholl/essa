#!/usr/bin/env python

"""
pythonconsoleplugin.py

A Python console custom widget plugin for Qt Designer.

Copyright (C) 2006 David Boddie <david@boddie.org.uk>
Copyright (C) 2005-2006 Trolltech ASA. All rights reserved.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

from PyQt4 import QtGui, QtDesigner
from dial_2 import Dial_2


class Dial_2Plugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    """PythonConsolePlugin(QtDesigner.QPyDesignerCustomWidgetPlugin)
    
    Provides a Python custom plugin for Qt Designer by implementing the
    QDesignerCustomWidgetPlugin via a PyQt-specific custom plugin class.
    """

    # The __init__() method is only used to set up the plugin and define its
    # initialized variable.
    def __init__(self, parent=None):
    
        super(Dial_2Plugin, self).__init__(parent)

        self.initialized = False

    # The initialize() and isInitialized() methods allow the plugin to set up
    # any required resources, ensuring that this can only happen once for each
    # plugin.
    def initialize(self, core):

        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):

        return self.initialized

    # This factory method creates new instances of our custom widget with the
    # appropriate parent.
    def createWidget(self, parent):
        return Dial_2(parent)

    # This method returns the name of the custom widget class that is provided
    # by this plugin.
    def name(self):
        return "Dial_2"

    # Returns the name of the group in Qt Designer's widget box that this
    # widget belongs to.
    def group(self):
        return "SCADA"

    # Returns the icon used to represent the custom widget in Qt Designer's
    # widget box.
    def icon(self):
        return QtGui.QIcon(_logo_pixmap)

    # Returns a short description of the custom widget for use in a tool tip.
    def toolTip(self):
        return ""

    # Returns a short description of the custom widget for use in a "What's
    # This?" help message for the widget.
    def whatsThis(self):
        return ""

    # Returns True if the custom widget acts as a container for other widgets;
    # otherwise returns False. Note that plugins for custom containers also
    # need to provide an implementation of the QDesignerContainerExtension
    # interface if they need to add custom editing support to Qt Designer.
    def isContainer(self):
        return False

    # Returns an XML description of a custom widget instance that describes
    # default values for its properties. Each custom widget created by this
    # plugin will be configured using this description.
    def domXml(self):
        return '<widget class="Dial_2" name="dial_2Widget">\n' \
               ' <property name="toolTip" >\n' \
               '  <string>Dial Widget 2</string>\n' \
               ' </property>\n' \
               ' <property name="whatsThis" >\n' \
               '  <string>SCADA Dial 2</string>\n' \
               ' </property>\n' \
               '</widget>\n'

    # Returns the module containing the custom widget class. It may include
    # a module path.
    def includeFile(self):
        return "dial_2"


# Define the image used for the icon.
_logo_16x16_xpm = [
    "16 16 75 1 ",
    "  c #DE0101",
    ". c #DF0101",
    "X c #E20101",
    "o c #E5180C",
    "O c #E61B0E",
    "+ c #E62417",
    "@ c #E72519",
    "# c #E7261A",
    "$ c #E72B1F",
    "% c #E73629",
    "& c #E83B31",
    "* c #EA4136",
    "= c #EA453A",
    "- c #EB4C42",
    "; c #EB4F46",
    ": c #EC4F46",
    "> c #EB5148",
    ", c #EB594E",
    "< c #EA5B52",
    "1 c #EC5E55",
    "2 c #EE635A",
    "3 c #ED655B",
    "4 c #EE665D",
    "5 c #EF665D",
    "6 c #ED6961",
    "7 c #EF746C",
    "8 c #F0766F",
    "9 c #F1837B",
    "0 c #F18881",
    "q c #F28982",
    "w c #F08C85",
    "e c #F18C86",
    "r c #F3938B",
    "t c #F39893",
    "y c #F39993",
    "u c #F49B95",
    "i c #F4A19B",
    "p c #F4A19D",
    "a c #F4A29C",
    "s c #F5A49F",
    "d c #F5A8A2",
    "f c #F5AAA6",
    "g c #F6ABA6",
    "h c #F6AAA7",
    "j c #F6AEAB",
    "k c #F6B4B0",
    "l c #F7B6B2",
    "z c #F8BBB7",
    "x c #F7BEBA",
    "c c #F8C5C3",
    "v c #F8C6C2",
    "b c #F9C6C3",
    "n c #F8C9C6",
    "m c #FACCC9",
    "M c #F9CECB",
    "N c #F9CFCC",
    "B c #FAD1CE",
    "V c #F9D2CF",
    "C c #F9D3D0",
    "Z c #FAD5D2",
    "A c #FBD8D5",
    "S c #F9DAD9",
    "D c #FCDAD9",
    "F c #FCDDDB",
    "G c #FBDEDC",
    "H c #FBDFDD",
    "J c #FCE6E5",
    "K c #FCE7E5",
    "L c #FDEAE8",
    "P c #FDEFED",
    "I c #FDEFEE",
    "U c #FDF0EE",
    "Y c #FEF4F4",
    "T c #FEFFFF",
    "R c gray100",
    "RRRRRRRRRRRRRRRR",
    "RRRRRRRH&aRRRRRR",
    "RRRRRRRR*X7RRRRR",
    "RRRRRRRRwuRRRRRR",
    "RRRRRRRw=fSRRRRR",
    "RRRRRRM$rt3RRRRR",
    "RRRRRRf9vAdHRRRR",
    "RRRRRRR%3luRRRRR",
    "RHRRRRf X0<RRRRR",
    "Ra6nA<  o3wRRRRR",
    "RRk>@+;+z7BRRRRR",
    "RRRRRRc;R93RRRRR",
    "RRRRRRMoPJaxJRRR",
    "RRRRRRB aRH;BRRR",
    "RRRRRRU,cRYjPRRR",
    "RRRRRRRMLRRRRRRR" ]
  

_logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)
