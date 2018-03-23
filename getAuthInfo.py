#!/usr/bin/python3
# This script retrieves UPnP configuration info and will parse the file for the PTP authentication data

# Import Dependencies
import requests
import xml.etree.ElementTree as ET

# initialize variables
server = "10.0.0.100"

# get xml file from server (note for actual use, port is 49152)
r = requests.get('http://' + server + ':49152/MobileDevDesc.xml')

# attempt to get file
if r.status_code != requests.codes.ok:
    exit("Unable to obtain device information, ensure camera is in pairing mode.")
else:
    print("Successfully retrieved info from " + server + "\n")

# Parse returned xml data
root = ET.fromstring(r.text)

# Retrieve relevant fields
uuid = root.find('{urn:schemas-upnp-org:device-1-0}device/{urn:schemas-upnp-org:device-1-0}UDN').text
#nickName = root.find('{urn:schemas-upnp-org:device-1-0}device/{urn:schemas-upnp-org:device-1-0}serviceList/{urn:schemas-upnp-org:device-1-0}service/{urn:schemas-canon-com:schema-upnp}X_deviceNickname').text
friendlyName = root.find('{urn:schemas-upnp-org:device-1-0}device/{urn:schemas-upnp-org:device-1-0}friendlyName').text

# note [5:] strips the first 5 chars from uuid which are 'uuid:'
print("uuid: " + uuid[5:])
print("Friendly Name: " + friendlyName)
#print("Device Nickname: " + nickName)
