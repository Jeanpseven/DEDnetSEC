import re
import subprocess

def get_networks():
    command = "netsh wlan show profiles"
    output = subprocess.check_output(command, shell=True).decode()
    network_profiles = re.findall("All User Profile     : (.*)\r", output)
    return network_profiles

def get_bssid(network_name):
    command = f"netsh wlan show profiles name=\"{network_name}\" keyMaterial"
    output = subprocess.check_output(command, shell=True).decode()
    bssid = re.search("BSSID 1             : (.*)\r", output).group(1)
    return bssid

def get_password(bssid):
    bssid_parts = bssid.split(":")
    last_octet = bssid_parts[-2] + bssid_parts[-1]
    password = last_octet.upper()
    return password

networks = get_networks()
for network in networks:
    bssid = get_bssid(network)
    password = get_password(bssid)
    print(f"Rede: {network}, BSSID: {bssid}, Senha: {password}")
