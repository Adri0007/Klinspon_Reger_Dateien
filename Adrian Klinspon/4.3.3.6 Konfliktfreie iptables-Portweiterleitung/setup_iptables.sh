#!/bin/bash
iptables -t nat -A PREROUTING -i wlan2 -p tcp --dport 80 -j REDIRECT --to-port 8080
