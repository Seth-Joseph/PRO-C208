import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def acceptConnections():
    global SERVER
    global clients

    while True:
        client,addr = SERVER.accept()
        print(addr)

def setup():
    print('\t\t\t\t\t\tMUSIC SHARE')

    global SERVER
    global IP_ADDRESS
    global PORT

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    SERVER.listen(100)

    print("\t\t\t\t\tWAITING FOR CONNECTIONS")

    acceptConnections()

setupThread = Thread(target=setup)
setupThread.start()