import socket
import network
from time import sleep_ms
import urequests as requests
from config import ssid, password


def connect_wifi():
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        return
    station.active(True)
    station.connect(ssid, password)
    i = 0
    while station.isconnected() == False:
        sleep_ms(100)
        i += 1
        if(i == 100):
            machine.reset()
        pass
    print('connected to '+ssid)
    res = requests.get(url='https://api.ipify.org/?format=text').text
    print('External IP:'+res)


connect_wifi()


cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    mensagem_envio = input("Digite a mensagem:")
    cliente.sendto(mensagem_envio.encode(), ("192.168.3.2", 12000))
    mensagem_bytes, endereco_ip_servidor = cliente.recvfrom(2048)
    print(mensagem_bytes.decode())
