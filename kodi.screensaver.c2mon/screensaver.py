#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmcaddon
import xbmcgui
import xbmc
import sys
import subprocess
import os

addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')
addon_path = addon.getAddonInfo('path') 
     
class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            self.exit_callback()

    def onInit(self):
        self.log('onInit')
        self.write('/sys/class/amhdmitx/amhdmitx0/phy', '0')
        self.exit_monitor = self.ExitMonitor(self.exit)

    def exit(self):
        self.abort_requested = True
        self.exit_monitor = None
        self.write('/sys/class/amhdmitx/amhdmitx0/phy', '1')
        self.log('exit')
        self.close()

    def log(self, msg):
        xbmc.log(u'c2mon hdmi screensaver: %s' % msg)

    def write(self, file, content):
        fd = os.open(file, os.O_WRONLY)                                                                                    
        os.write(fd, content)                                                                                                                                                
        os.close(fd)                                                                                                                                                          
        del fd        


if __name__ == '__main__':
    screensaver = Screensaver(
        'script-main.xml',
        addon_path,
        'default',
    )
    screensaver.doModal()
    del screensaver
    sys.modules.clear()