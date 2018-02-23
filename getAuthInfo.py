#!/usr/bin/python3
# This script retrieves UPnP configuration info and will parse the file for the PTP authentication data

# Import Dependencies
import requests
import xml.etree.ElementTree as ET

server = 192.168.1.100

# get xml file from server (note for actual use, port is 49152)
r = request.get('http://' + server + '/CameraDevDesc.xml')

if r.status_code != requests.codes.ok:
    exit("Unable to obtain device information, ensure camera is in pairing mode.")

# Parse returned xml data
root = ET.fromstring(r.text)

guid = root.find('UDN')

print guid.attrib
