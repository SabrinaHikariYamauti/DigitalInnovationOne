import os#Importa módulo ou biblioteca os (integra os programas e recursos do S.O)
import time

print("#"*60)

ip_ou_host  =input("Digite o IP ou host a ser verificado: ")

os.system('ping -n 6 {}'.format(ip_ou_host))#chamado system da biblioteca os(chamando um comando ping que mostrará número de pacotes)
