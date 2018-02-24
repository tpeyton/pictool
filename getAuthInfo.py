#!/usr/bin/python3
# This script retrieves UPnP configuration info and will parse the file for the PTP authentication data

# Import Dependencies
import requests
import xml.etree.ElementTree as ET

server = "192.168.1.100"

# get xml file from server (note for actual use, port is 49152)
r = requests.get('http://' + server + '/CameraDevDesc.xml')

if r.status_code != requests.codes.ok:
    exit("Unable to obtain device information, ensure camera is in pairing mode.")
else:
    print("Successfully retrieved info from " + server + "\n")

# Parse returned xml data
root = ET.fromstring(r.text)

# reference for XML parsing: https://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree
#tree = ET.parse('CameraDevDesc.xml')
#root = tree.getroot()


uuid = root.find('{urn:schemas-upnp-org:device-1-0}device/{urn:schemas-upnp-org:device-1-0}UDN').text

friendlyName = root.find('{urn:schemas-upnp-org:device-1-0}device/{urn:schemas-upnp-org:device-1-0}friendlyName').text

print(uuid)
print(friendlyName)
