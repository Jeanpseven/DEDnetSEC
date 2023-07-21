# DEDnetSEC
# wifucker.py
testa senhas baseado em um algoritmo usado em wifis não tão seguros,que não tem seu nome e senha alterados(padrão),fazendo um calculo com BSSID e SSID estudado por mim

foi modificado para celulares pra vc sair hackeando wifis como um verdadeiro insurgente do dedsec,muito util em casos de emergência
_______________________________________
# wifucker2.0.py

o wifucker2.0 mostra dispositivos locais (util pra hackear cameras,usando o script wannasee no repositorio Jeanseven/BruteCam (https://github.com/Jeanpseven/BruteCam)
_______________________________________
# wifucker3.0.py
# Conexão Automática a Redes Wi-Fi usando PyWiFi

Este é um script Python que automatiza o processo de conexão a redes Wi-Fi utilizando a biblioteca PyWiFi. O script faz a varredura das redes Wi-Fi disponíveis, calcula a senha com base no BSSID (endereço MAC do ponto de acesso) e conecta-se automaticamente às redes encontradas.

## Funcionalidades

- Varre e lista as redes Wi-Fi disponíveis.
- Calcula a senha com base no BSSID do ponto de acesso.
- Conecta-se automaticamente às redes Wi-Fi com a senha calculada.
- Obtém a lista de dispositivos conectados na rede local.

## Pré-requisitos

Antes de executar o script, é necessário ter as seguintes bibliotecas instaladas:

- pywifi
- scapy

## Uso

1. Clone o repositório e acesse o diretório do projeto.
2. Execute o script `wifucker3.0.py` usando o Python 3.
3. O script irá varrer e listar as redes Wi-Fi disponíveis.
4. Será feito o cálculo da senha com base no BSSID de cada rede.
5. O script irá se conectar automaticamente às redes usando a senha calculada.
6. Será exibida a lista de dispositivos conectados à rede local.

## oque há de novo?
o script roda em segundo plano e obtém as redes de wifi automaticamente sem precisar e vc rodando o script,ou seja enquanto vc anda pela rua o script calcula as senhas das redes de wifi mais fracas a ser atacadas

## Contribuição

Sinta-se à vontade para contribuir para o aprimoramento deste script. Caso encontre algum problema ou tenha alguma sugestão, por favor, abra uma nova issue ou envie um pull request.
_______________________________________
# wifucker4

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
