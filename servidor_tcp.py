import socket
from threading import Thread

def tratar_cliente(socket_cliente, endereco_cliente):
    print(f"TCP: Conexão estabelecida com {endereco_cliente}")
    try:
        dados = socket_cliente.recv(1024).decode()
        print(f"Recebido de {endereco_cliente}: {dados}")
        resposta = f"TCP: {dados}"
        socket_cliente.send(resposta.encode())
    finally:
        socket_cliente.close()
        print(f"TCP: Conexão encerrada com {endereco_cliente}")
def iniciar_servidor_tcp():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('0.0.0.0', 5000))
    servidor.listen()
    print("Servidor TCP ouvindo na porta 5000")
    while True:
        socket_cliente, endereco_cliente = servidor.accept()
        thread_cliente = Thread(target=tratar_cliente, args=(socket_cliente, endereco_cliente))
        thread_cliente.start()

if __name__ == "__main__":
    iniciar_servidor_tcp()
