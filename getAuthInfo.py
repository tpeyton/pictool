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

#for child in root:
#    print(child.tag, child.attrib)

#print(root[2][7].text)

for elem in root:
    for subelem in elem:
        print(subelem.tag, subelem.text)



#print(guid)
