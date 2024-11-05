import socket

def iniciar_servidor_udp():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind(('0.0.0.0', 5001))
    print("Servidor UDP está ouvindo na porta 5001")

    while True:
        dados, endereco_cliente = servidor.recvfrom(1024)
        print(f"Mensagem recebida de {endereco_cliente}: {dados.decode()}")
        resposta = f"UDP: {dados.decode()}"
        servidor.sendto(resposta.encode(), endereco_cliente)

if __name__ == "__main__":
    iniciar_servidor_udp()
