import socket
from threading import Thread
def tratar_cliente_tcp(socket_cliente, endereco_cliente):
    print(f"Nova conexão TCP de {endereco_cliente}")
    try:
        dados = socket_cliente.recv(1024).decode()
        print(f"Mensagem recebida de {endereco_cliente}: {dados}")
        resposta = f"TCP: {dados}"
        socket_cliente.send(resposta.encode())
    finally:
        socket_cliente.close()
        print(f"Conexão TCP encerrada com {endereco_cliente}")

def servidor_tcp():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(('0.0.0.0', 5000))
    tcp_socket.listen()
    print("Servidor TCP está ouvindo na porta 5000")

    while True:
        socket_cliente, endereco_cliente = tcp_socket.accept()
        thread_cliente = Thread(target=tratar_cliente_tcp, args=(socket_cliente, endereco_cliente))
        thread_cliente.start()
def servidor_udp():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('0.0.0.0', 5001))
    print("Servidor UDP está ouvindo na porta 5001")
    while True:
        dados, endereco_cliente = udp_socket.recvfrom(1024)
        print(f"Mensagem recebida de {endereco_cliente}: {dados.decode()}")
        resposta = f"UDP: {dados.decode()}"
        udp_socket.sendto(resposta.encode(), endereco_cliente)
def iniciar_servidor_combinado():
    thread_tcp = Thread(target=servidor_tcp)
    thread_udp = Thread(target=servidor_udp)
    thread_tcp.start()
    thread_udp.start()
    thread_tcp.join()
    thread_udp.join()

if __name__ == "__main__":
    iniciar_servidor_combinado()
