# python -m pip install ifaddr
# python -m pip install icmplib
# python -m pip install ipaddress

import socket
from multiprocessing import Process
import ifaddr
# python -m pip install ipaddress
from ipaddress import IPv4Address, IPv4Network, IPv4Interface


def calculaBroadcast(ip_mask):
    ifc = IPv4Interface(ip_mask)
    print(ifc.ip)
    print(ifc.network)
    ip = IPv4Address(ifc.ip)
    print(f'Loopback {ip.is_loopback} Privado: {ip.is_private}')
    print(IPv4Network(ifc.network).broadcast_address)



# Essa função mostra todas as interfaces neste computador
def mostraips():
    adapters = ifaddr.get_adapters()

    for adapter in adapters:
        print("\nNIC: " , adapter.nice_name)
        for ip in adapter.ips:
            print(ip.ip,"/", ip.network_prefix)            
    print('-----------------')

# Essa função mostra o IP associado ao nome do computador
def mostraip():
    hostname = socket.gethostname()    
    hostip = socket.gethostbyname(hostname)
    print('host: {} ip: {}'.format(hostname, hostip))

# Essa função simula o comportamento de um dispositivo de IOT em uma LAN
def receptor(host, porta, id):
    print(id, ' foi iniciado')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind((host,porta))
    except:
        print('erro de bind')

    while True:
        data, addr = s.recvfrom(1024)
        print(id, ': ' , addr, ' enviou ', data)
        s.sendto(id.encode() , addr )

if __name__ == '__main__':
    mostraip()
    Process(target=receptor, args=('',9999,'portaria')).start()
    Process(target=receptor, args=('127.0.0.2', 9999,'sala')).start()
    Process(target=receptor, args=('127.0.0.3', 9999,'quarto')).start()
    Process(target=receptor, args=('127.0.0.4', 9999,'cozinha')).start()# python -m pip install ifaddr
    calculaBroadcast("10.150.8.93")
# python -m pip install icmplib
# python -m pip install ipaddress

import socket
from multiprocessing import Process
import ifaddr


# Essa função mostra todas as interfaces neste computador
def mostraips():
    adapters = ifaddr.get_adapters()

    for adapter in adapters:
        print("\nNIC: " , adapter.nice_name)
        for ip in adapter.ips:
            print(ip.ip,"/", ip.network_prefix)            
    print('-----------------')

# Essa função mostra o IP associado ao nome do computador
def mostraip():
    hostname = socket.gethostname()    
    hostip = socket.gethostbyname(hostname)
    print('host: {} ip: {}'.format(hostname, hostip))

# Essa função simula o comportamento de um dispositivo de IOT em uma LAN
def receptor(host, porta, id):
    print(id, ' foi iniciado')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind((host,porta))
    except:
        print('erro de bind')

    while True:
        data, addr = s.recvfrom(1024)
        print(id, ': ' , addr, ' enviou ', data)
        s.sendto(id.encode() , addr )

if __name__ == '__main__':
    mostraip()
    Process(target=receptor, args=('',9999,'portaria')).start()
    Process(target=receptor, args=('127.0.0.2', 9999,'sala')).start()
    Process(target=receptor, args=('127.0.0.3', 9999,'quarto')).start()
    Process(target=receptor, args=('127.0.0.4', 9999,'cozinha')).start()
    print()
    
