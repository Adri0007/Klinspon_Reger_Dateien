from scapy.all import *
import time

iface = "wlan2"

try:
    ap_mac = get_if_hwaddr(iface)
except Exception:
    ap_mac = "ff:ff:ff:ff:ff:ff"

src_ip = "192.168.43.99"
dst_ip = "192.168.43.1"

http_payload = (
    "POST /login HTTP/1.1\r\n"
    f"Host: {dst_ip}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    "Content-Length: 42\r\n"
    "\r\n"
    "username=admin&password=SuperSecretPassword!"
)

pkt = Ether(src=ap_mac, dst="ff:ff:ff:ff:ff:ff") / IP(src=src_ip, dst=dst_ip) / \
            TCP(sport=54321, dport=80, flags="PA", seq=1000, ack=1000) / Raw(load=http_payload)

time.sleep(5)

while True:
    try:
        sendp(pkt, iface=iface, verbose=False)
    except Exception as e:
        pass
    time.sleep(10)
