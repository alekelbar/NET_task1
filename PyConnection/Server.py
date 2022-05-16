from PyTranslate.decode import decode
import socket
from Client import initClient
from definePass import setEncoding


def initServer(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)  # cantidad de peticiones

    bandera = True
    msg_recv = ''

    while bandera:
        # establecer conexión
        (c, addr) = s.accept()
        print(f"Se establecio conexión con: {addr}")

        msg = f"Conexión establecida con: {socket.gethostname()}"
        c.send(msg.encode("utf-8"))

        # decodificar el mensaje recibido
        msg_recv = c.recv(1024).decode("ascii")
        msg_recv = decode(msg_recv, setEncoding('352'))
        print(msg_recv)
        c.close()
    #     bandera = False
    # # segunda parte, conectarse a otro servidor...
    # host = ''

    # initClient(host, port, msg_recv)


if __name__ == "__main__":
    host = '25.7.98.255'
    port = 44440
    initServer(host, port)
