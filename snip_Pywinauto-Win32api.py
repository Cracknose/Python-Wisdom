#! python3
# Copy of SysInfo_0.1.py for Snippets

from pywinauto import application
import time
from win32api import keybd_event
import os

# VARS
cwd = os.getcwd()
cwd = cwd + "\\"
app = application.Application()
LogLvl = 1


# FUNCTIONS

def SaveFile(data, filename):
	fullname = cwd + filename
	file = open(fullname, 'w')
	file.write(data)
	file.close
	print("Data saved to file: ")
	print("   " + fullname)

def PrintLog(msg):
	if LogLvl != 0:
		print(msg)


def PressEnter():
	# Key down enter
	keybd_event(13, 0, 2, 0)
	# Key up enter 
	keybd_event(13, 0, 1, 0)

def GetLicenses():
	# Get current directory and add filename	
	filename_license = cwd + "Licenses.txt"

	#if key allready exits THEN skip
	if os.path.isfile(filename_license) == 1:
		print("file already there, skipping...")
		# End function early
		return

	# Start & Focus ProduKey.exe	
	app.start("ProduKey.exe")
	app.ProduKey.MenuSelect("File ->Save All Items")	

	# Save File , Window name is = "Select a filename to save"
	app.Selectafilenametosave.edit.SetText(filename_license)
	PressEnter()

	# Exit ProduKey.exe
	app.ProduKey.SetFocus()
	app.ProduKey.MenuSelect("File ->Exit")

	# Check to see if file has been written
	time.sleep(1)
	if os.path.isfile(filename_license) == 0:
		print("Err: File not found! retrying")
		GetLicenses()
	else:
		print("Success: File Found")


def RunRun():
	# RUN RUN
	# Windows button down (91)
	keybd_event(91, 0, 2, 0)
	# R key down (82)
	keybd_event(82, 0, 2, 0)
	# Windows button up
	keybd_event(91, 0, 1, 0)
	# R key up
	keybd_event(82, 0, 1, 0)

def RunCMD(cmd, filename):	

	process = os.popen(cmd)
	data = process.read()
	process.close()

	SaveFile(data, filename)  # This isent all installed but a good start
	# Save Data To File



GetLicenses()
RunCMD("wmic startup get caption,command,location", "Autostart.txt")
RunCMD("wmic product get name", "Software.txt")
