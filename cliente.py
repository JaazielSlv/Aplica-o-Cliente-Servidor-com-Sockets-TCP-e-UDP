import socket

def cliente_tcp(mensagem):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect(('127.0.0.1', 5000))
        cliente.send(mensagem.encode())
        resposta = cliente.recv(1024).decode()
        print(f"Resposta do servidor: {resposta}")

def cliente_udp(mensagem):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cliente:
        cliente.sendto(mensagem.encode(), ('127.0.0.1', 5001))
        resposta, _ = cliente.recvfrom(1024)
        print(f"Resposta do servidor: {resposta.decode()}")

def main():
    protocolo = input("Escolha o protocolo (TCP ou UDP): ").strip().upper()
    mensagem = input("Digite a mensagem para enviar ao servidor: ")

    if protocolo == "TCP":
        cliente_tcp(mensagem)
    elif protocolo == "UDP":
        cliente_udp(mensagem)
    else:
        print("Protocolo inválido. Escolha TCP ou UDP.")

if __name__ == "__main__":
    main()
