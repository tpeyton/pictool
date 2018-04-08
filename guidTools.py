#!/usr/bin/python
import os

def formatGUID(guid):
    # remote hyphens from guid pulled from xml
    guid = guid.translate(None, "-")

    # format guid in colon form for gphoto2 settings file
    guid = ':'.join([guid[i:i+2] for i in range(0, len(guid), 2)])

    return guid

def setGUID(settingsPath,guid):
    # initialize temp settings file
    tempSettingsPath = settingsPath + "2"

    # open files needed
    settings = open(settingsPath, "r")
    tempSettings = open(tempSettingsPath, "a")

    for line in settings:
        if not line.startswith('ptp2_ip=guid='):
            tempSettings.write(line)

    # write new guid to file
    tempSettings.write('ptp2_ip=guid=' + guid +'\n')

    # close files after writing
    settings.close()
    tempSettings.close()

    # delete old gphoto2 settings
    os.remove(settingsPath)

    # rename newSettings to settings
    os.rename(tempSettingsPath,settingsPath)
