import socket#relaciona a placa de rede e sistema operacional
#é uma API que realiza abertura e fechamento de conexão
import sys #fornece acesso àlgumas variáveis e funções que tem forte interação com interpretador python

def main():#tentar uma conexão tcp ip
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #define tipo de conexão(protocolo ip),
        #define que é tcp, define a comuicação com servidor 0
    except socket.error as e:
        print("A conexão falhou!!")
        print("Erro:{}".format(e))
        sys.exit()
    print("Socket criado com sucesso")

    HostAlvo = input("Digite o host ou ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try: 
        s.connect((HostAlvo,int(PortaAlvo)))
        print("Cliente TCP conectado com Sucesso no Host "+HostAlvo+ " e na porta: "+ PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no Host")
        print("Erro:{}".format(e))
        sys.exit()

if __name__=="__main__":
    main()
