from PyTranslate.decode import decode
import socket
from Client import initClient
from definePass import setEncoding


def initServer(host, port, password):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)  # cantidad de peticiones

    msg_recv = ''
    # establecer conexión
    (c, addr) = s.accept()
    print(f"Se establecio conexión con: {addr}")

    msg = f"Conexión establecida con: {socket.gethostname()}"
    c.send(msg.encode("utf-8"))

    # decodificar el mensaje recibido
    msg_recv = c.recv(1024).decode("ascii")
    msg_recv = decode(msg_recv, setEncoding(password))
    print(msg_recv)
    c.close()
    # segunda parte, conectarse a otro servidor... Convertirse en cliente
    host = '25.14.79.15'  # siguiente host
    port = 9090  # Siguiente puerto
    nextPassword = '759'
    initClient(host, port, msg_recv, nextPassword)  # next password


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 44440
    password = '352'
    initServer(host, port, password)
