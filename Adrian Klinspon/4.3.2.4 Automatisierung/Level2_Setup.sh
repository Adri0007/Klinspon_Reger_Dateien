#!/bin/bash

iptables -D INPUT -i wlan0 -m mac ! --mac-source 3c:52:a1:2a:bb:bb -j DROP 2>/dev/null
iptables -I INPUT -i wlan0 -m mac ! --mac-source 3c:52:a1:2a:bb:bb -j DROP

pkill -f "wpa_supplicant -B -i wlan1"
pkill -f "ping -b 10.99.99.255"

nmcli device set wlan1 managed no 2>/dev/null
sleep 1

ip link set wlan1 down 2>/dev/null
ip link set wlan1 address 3c:52:a1:2a:bb:bb
ip link set wlan1 up

wpa_supplicant -B -i wlan1 -c /etc/wpa_supplicant/Level2_client.conf
sleep 5

ip addr flush dev wlan1 2>/dev/null
ip addr add 10.99.99.10/24 dev wlan1

ping -b 10.99.99.255 -I wlan1 > /dev/null 2>&1 &
