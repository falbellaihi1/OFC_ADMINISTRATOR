import cv2

import numpy as np
import cv2
import subprocess
import os

import logging

import pywinauto
from pywinauto import timings
from pywinauto import Desktop
from pywinauto.application import Application
# app = Application(backend="uia").start(r'C:\Program Files (x86)\Origin\Origin.exe')
# app = Desktop(backend="uia").window(title_re="Origin", found_index=0)
#
# # describe the window inside Notepad.exe process
# # app = app.TBPanel2.wrapper_object()
#
# app = app.TBPanel2.wait('ready', timeout=10) # if you need non-default time to wait
#
# dlg_spec = app.Origin
# # wait till the window is really open
# actionable_dlg = dlg_spec.wait('visible')
# timings.Timings.Slow()
# dlg_spec.wrapper_object().minimize() # while debugging
#
#

from subprocess import Popen
from pywinauto import Desktop

# Popen(r"C:\Program Files (x86)\Origin\Origin.exe", shell=True)
# dlg = Desktop(backend="uia").Origin
# dlg.wait('visible')
# dlg.select()
# elem = pywinauto.findwindows.find_element(title_re='Origin', found_index  =0)
#
# print('you need to print it ',elem)

# dlg.wait('visible')
# dlg.window(auto_id='num8Button', control_type='Button')





# app = Application(backend="uia").start('notepad.exe')
#
# # describe the window inside Notepad.exe process
# dlg_spec = app.UntitledNotepad
# # wait till the window is really open
# actionable_dlg = dlg_spec.wait('visible')
#
# from pywinauto.application import Application
#
# app = Application().start(r"C:\Program Files (x86)\Origin\Origin.exe")
# dlg_spec = app.window(title='Origin')
# dlg_spec.wrapper_object().minimize() # while debugging




# app.Edit.type_keys("pywinauto Works!", with_spaces = True)

# #os.startfile(r"C:\Program Files (x86)\Origin Games\Battlefield V\bfv.exe")
# username = 'falbellaihi@hotmail.com'
# password = 'AAA'
# cmd = r"C:\Program Files (x86)\Origin Games\Battlefield V\bfv.exe"
# p = subprocess.Popen(cmd, stdin=subprocess.PIPE, shell=True)
# Properties = Desktop(backend='uia').Common_Files_Properties
# Properties.print_control_identifiers()