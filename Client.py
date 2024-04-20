import socket

HEADERSIZE = 10

ipv4 = input("which ip we gonna connect to: ")
port = int(input("Which Port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # like we said before

s.connect((ipv4, port))# if we're in the same network we can use socket.gethostname() and we can define the port

print("Connecting......")

while True:
        full_msg = ''
        new_msg = True

while True: # to continue reciving any data while there's a conncetion
        msg = s.recv(1024) # chunks of data we're going to recive
        if new_msg:
                print(f"new message length: {msg[:HEADERSIZE]}")
                msglen = int(msg[:HEADERSIZE])
                full_msg += msg.decode("UTF-8") # decoding the message with UTF-8
                print(full_msg) 
