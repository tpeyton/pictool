#!/usr/bin/python
# This script is for reference purposes and demonstrates how to parse an xml tree and search for tags of interest

# Import Dependencies
import xml.etree.ElementTree as ET

# reference for XML parsing: https://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree
# another one: https://docs.python.org/3/library/xml.etree.elementtree.html
tree = ET.parse('camera-CameraDevDesc.xml')
root = tree.getroot()

# iterate through all levels of tree
for child in root:
    for sub in child:
        for sub2 in sub:
            for sub3 in sub2:
                print sub3.tag, sub3.attrib, sub3.text


nickName = root.find('{urn:schemas-upnp-org:device-1-0}device/{urn:schemas-upnp-org:device-1-0}serviceList/{urn:schemas-upnp-org:device-1-0}service/{urn:schemas-canon-com:schema-upnp}X_deviceNickname').text

print(nickName)
