import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT)
FORMAT = "utf-8"
DC_MSG = "Bye"

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def Client_handle(conn , addr) : 
    print("[NEW CONNECTION] {addr} connected ! ")
    connect = True 
    while connect :
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length :
            
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT )
            print(f"[{addr}] {msg}")
            if msg == DC_MSG :
                connect = False
            conn.send("[RECIVED]".encode(FORMAT))
                
    conn.close()


def start() :
    server.listen() 
    print(f"[LISTENING] {SERVER}")
    while True : 
        conn , addr = server.accept()
        thread = threading.Thread(target=Client_handle , args=(conn , addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is loading...")

start()