from wifi import Cell
import pywifi
from pywifi import const
import time

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    iface.disconnect()
    time.sleep(1)
    
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(5)
    
    if iface.status() == const.IFACE_CONNECTED:
        print("Conectado à rede Wi-Fi com sucesso!")
    else:
        print("Falha ao conectar à rede Wi-Fi.")

def list_wifis():
    cells = Cell.all('wlan0')
    print("Redes Wi-Fi disponíveis:")
    for i, cell in enumerate(cells):
        if cell.encryption_type == 'wep' or cell.encryption_type == 'wpa':
            print(f"{i+1}. {cell.ssid} ({cell.encryption_type})")

def choose_wifi():
    while True:
        try:
            choice = int(input("Escolha o número da rede Wi-Fi desejada: "))
            if choice < 1 or choice > len(Cell.all('wlan0')):
                print("Escolha um número válido.")
            else:
                return choice
        except ValueError:
            print("Por favor, insira um número válido.")

def get_bssid(choice):
    cells = Cell.all('wlan0')
    return cells[choice - 1].address

def get_ssid(choice):
    cells = Cell.all('wlan0')
    return cells[choice - 1].ssid

def calculate_password(bssid, ssid):
    last_two_digits_ssid = ssid[-2:]
    last_two_digits_bssid = bssid[-2:].replace(":", "")
    bssid_trimmed = bssid[2:]
    password = ssid[:-2] + last_two_digits_bssid + bssid_trimmed
    return password

list_wifis()
choice = choose_wifi()
bssid = get_bssid(choice)
ssid = get_ssid(choice)
password = calculate_password(bssid, ssid)

print("\nInformações da rede Wi-Fi escolhida:")
print("BSSID:", bssid)
print("SSID:", ssid)
print("Senha calculada:", password)

connect_to_wifi(ssid, password)
