import cx_Freeze
import sys
import win32con
import pythoncom
import pywintypes
import win32com.server.policy
import paramiko
import os
import PIL

base= None
executables = [cx_Freeze.Executable("MainApp.py",base=base,icon="SSC_Circle.ico")]
cx_Freeze.setup(name = "WesternSSC"
				,options = {"build_exe":{"packages":["tkinter","win32con","paramiko","PIL"],"include_files":["SSC_Circle.ico"]}}
				,version="0.01"
				,description="Fuck you sam"
				,executables= executables
				)
