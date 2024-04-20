import socket # including the lib we need to use

HEADERSIZE = 10

address = input("What's Da IP: ")
port = int(input("What's Da PORT: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # we need to define the socket object
# AF_INET stands for standard family for ipv4 we can use AF_INET6 or AF_BLUETOOTH for different family
# SOCK_STREAM included to use TCP

s.bind((address, port)) # we're going to bind it into a tuple for ip & port 

s.listen(5) # we're going to listen to the connection with a queue of five 5

while True:
    connection, address = s.accept() # connection is a socket object we will use to send and recive connection , address it contain the client address ( what's the address he came from )
    print(f"connection from {address} has been established!") # look at the excelimation mark this is a serious business
    msg = "Welcome To The Server"
    msgg = f'{len(msg):<{HEADERSIZE}}'+msg
    connection.send(bytes("Welcome To the Server", "UTF-8")) # we're going to send a message to the client to confirm the connection through a bytes with a UTF-8 type
    connection.close()
		
