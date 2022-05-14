import socket


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER , PORT)
FORMAT = "utf-8"
DC_MSG = "Bye"

Client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
Client.connect(ADDR)


def send(msg) :
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '* (HEADER - len(send_length))
    Client.send(send_length)
    Client.send(message)
    print(Client.recv(2040).decode(FORMAT))
    
    
    
def Tracker(msg) :
    if(msg == "exit") :
        send(DC_MSG)
    else :
        send(msg)

        
        
while True : 

    inpt = input("Enter your message please : ")
    if(inpt == "exit") :
        Tracker(inpt)
        break
    Tracker(inpt)
