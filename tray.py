#!/usr/bin/env python3
# coding=utf-8

from tkinter import *
from pystray import Icon as icon, Menu as menu, MenuItem as item
import pystray
from PIL import Image
import sys

window = Tk()

def quit_window():
  sys.exit()

def hide_window():
    window.withdraw()
    items = []
    items.append(pystray.MenuItem('Quit', quit_window))
    image=Image.open('./app.png')
    icon=pystray.Icon("name", image, "title", items)
    icon.run()

window.protocol('WM_DELETE_WINDOW', hide_window)
window.mainloop()
