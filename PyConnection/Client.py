import socket
from PyTranslate.encode import encode
from definePass import *


def initClient(host, port, msg_env, password):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, port))
    msg_rec = c.recv(1024)
    print(msg_rec.decode('utf-8'))
    # codificar el mensaje enviado
    msg_env = encode(msg_env, setEncoding(password))
    c.send(msg_env.encode('ascii'))
    c.close()


if __name__ == '__main__':
    host = '25.14.79.15'
    port = 8080
    msg = ""
    while True:
        msg = input("Digite el mensaje a enviar: ")
        initClient(host, port, msg, '352')
