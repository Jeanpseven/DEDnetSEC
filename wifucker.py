import pywifi

# Inicializa o objeto Wifi
wifi = pywifi.PyWiFi()

# Obtém a primeira interface Wi-Fi disponível
iface = wifi.interfaces()[0]

# Ativa a interface
iface.enable()

# Obtém a lista de redes Wi-Fi disponíveis
networks = iface.scan_results()

# Imprime a lista numerada de redes
for i, network in enumerate(networks, 1):
    print(f"{i}. SSID: {network.ssid} - BSSID: {network.bssid}")

# Obtém a escolha do usuário
choice = int(input("Escolha o número da rede Wi-Fi desejada: "))

# Verifica se o número de escolha é válido
if choice < 1 or choice > len(networks):
    print("Opção inválida!")
else:
    # Obtém a rede escolhida
    chosen_network = networks[choice - 1]

    # Remove os ":" do BSSID
    bssid = chosen_network.bssid.replace(":", "")

    # Remove os dois primeiros números do BSSID
    bssid = bssid[2:]

    # Imprime as informações da rede escolhida com as modificações
    print(f"\nSSID: {chosen_network.ssid}")
    print(f"BSSID: {bssid}")
    print(f"Signal Strength: {chosen_network.signal}")

    # Conecta-se à rede escolhida (exemplo)
    # Essa parte precisa ser ajustada para conectar-se à rede corretamente
    # iface.connect(chosen_network.ssid, chosen_network.bssid)
