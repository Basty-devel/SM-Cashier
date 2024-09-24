# SM-Cashier
#
#  cashier.py and cashier.sh
#  
#  Copyright 2024  <snestler@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
As former 3rd Level Supporter at GK Software SE the first project in PythonX was a bit familiar to me. It is far away from perfect but the GUI works and the project Supermarket Cashier is extensible in any direction..
Logic is written in Python and the GUI is Tinkter. All crossplatform made. Feel free to add functionality like VAT.


Linux:

The command to start the script in Linux is : bash cashier.sh . It start a virtual enviroment, checks and installs dependencies(Tinkter) and runs the cashier.py file. Afterclosing the GUI the venv is deactivated and You can go on as usual.
Make sure You have saved all files in the same folder.

MacOS & Windows:

Tinkter comes with python per default on these OSs and it should work if python3 is regulary installed.
Command: python3 cashier.py . (You do not need the Shellscript!)
