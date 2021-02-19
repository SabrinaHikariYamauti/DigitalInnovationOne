import ipaddress #manupilação, calculo de ip, redes
#ip = '192.168.0.1'

#imprimir como ip
#endereco = ipaddress.ip_address(ip)

#print(endereco+257)

ip = '192.168.0.100/24'

rede = ipaddress.ip_network(ip, strict = False)
print(rede)
