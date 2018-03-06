#!/bin/bash

# Initialize variables
MONITOR=wlan1

# Configure monitoring interface
ifconfig $MONITOR 10.0.0.1/24 up

hostapd /etc/hostapd/hostapd.conf -B
#tshark -i $MONITOR -w capture.pcap -P
