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
Logic is written in Python and the GUI is Tinkter. All crossplatform made. Pi 4B ready with free open source OSs. 

Unlock the Power of Efficient Collaboration with SM-Cashier on GitHub!

Welcome to SM-Cashier, your ultimate tool for retail software. Built with passion and precision, SM-Cashier streamlines in calculating prices, discounts, taxes or what ever You want. It is just the beginning and a solid base for further process, empowering developers and teams to achieve more with less effort.

Why SM-Cashier?
💡 Innovative Features: Leverage cutting-edge tools designed to boost productivity and enhance your workflow.
⚙️ Seamless Integration: Effortlessly integrate with your favorite technologies and services to make your work smoother and faster.
🛡️ Rock-Solid Security: Built with security at its core, SM-Cashier ensures your code is safe while maintaining complete control.
🌐 Open Source Excellence: Collaborate with a vibrant community of contributors who are as passionate about innovation as you are.
Key Highlights:
📈 Scalable Performance which is crossplatform: Optimized for both small teams and enterprise-level projects, ensuring reliability at any scale. It runs on Debian and was tested on a Raspberry Pi 4B, which means no license costs for Software and pretty less for hardware.
⏱️ Time-Saving Automation: Automate repetitive tasks, minimize errors, and maximize efficiency.
💬 Active Community Support: Join a thriving ecosystem of users and contributors who are ready to collaborate, solve problems, and innovate together.


Linux:

The command to start the script in Linux is : bash cashier.sh . It start a virtual enviroment, checks and installs dependencies(Tinkter) and runs the cashier.py file. Afterclosing the GUI the venv is deactivated and You can go on as usual.
Make sure You have saved all files in the same folder.

MacOS & Windows:

Tinkter comes with python per default on these OSs and it should work if python3 is regulary installed.
Command: python3 cashier.py . (You do not need the Shellscript!)
