# DEDnetSEC

# wifucker

O script é uma ferramenta de linha de comando desenvolvida para fins educacionais e demonstrativos, denominada "DEDSEC WIFI ATTACK". Sua função é automatizar a identificação e possível quebra de senhas de redes Wi-Fi protegidas pelo protocolo WPA/WPA2 utilizando a vulnerabilidade do WPS (Wi-Fi Protected Setup).

O script foi dividido em várias funções para tornar o código mais organizado e legível. Aqui está uma descrição geral das principais funções do script:

check_root(): Essa função verifica se o script está sendo executado com privilégios de superusuário (root) para que seja possível manipular as interfaces de rede e realizar escaneamentos. Caso o script não esteja sendo executado como root, ele é encerrado com uma mensagem de erro.

menu(): Essa função é o ponto central do script e exibe o menu principal. Ele permite ao usuário escolher entre iniciar o escaneamento e ataque de redes Wi-Fi ou sair do programa.

show_wifi(): Essa função lista as interfaces de rede Wi-Fi disponíveis no sistema para que o usuário possa escolher qual delas será utilizada durante o escaneamento.

mon_man_mode(wname, mode): Essa função coloca a interface Wi-Fi selecionada pelo usuário no modo monitor ou modo gerenciado, dependendo do argumento mode fornecido. Isso permite ao script capturar pacotes e realizar outras operações durante o escaneamento.

scanAP(wname): Essa função inicia o escaneamento das redes Wi-Fi disponíveis na área utilizando o comando airodump-ng. O script analisa os resultados do escaneamento e lista as redes Wi-Fi encontradas, exibindo informações como SSID, canal, encriptação e potência do sinal. O usuário pode interromper o escaneamento pressionando Ctrl+C quando a rede alvo desejada for encontrada.

selectAP(proc_read, output_clients, bssid_list, ssid_list, channel_list): Essa função permite ao usuário selecionar a rede Wi-Fi alvo a ser atacada, fornecendo o número correspondente à rede na lista exibida anteriormente. Após a seleção, inicia-se o ataque de quebra de senha utilizando a ferramenta reaver.

attack(target_bssid, target_ssid, target_channel, wname): Essa função executa o ataque de quebra de senha utilizando o protocolo WPS contra a rede Wi-Fi alvo selecionada. O ataque é realizado com o comando reaver, que tenta encontrar a senha do roteador Wi-Fi através de um processo de força bruta.

password_show(): Após o ataque ser concluído, essa função mostra a senha do roteador Wi-Fi se ela for bem-sucedida. Caso contrário, exibe uma mensagem informando que a senha não foi encontrada.

Além das funções relacionadas ao ataque Wi-Fi, o script também possui funções de verificação e instalação de dependências necessárias, bem como funções auxiliares para obter os dispositivos conectados à rede Wi-Fi e calcular a senha Wi-Fi com base no BSSID (Basic Service Set Identifier) do roteador.
