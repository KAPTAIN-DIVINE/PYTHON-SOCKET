import socket
# i just imported the socket package
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# An instance of the socket has been created and represented as server
print("Socket has been created...")
Host = "127.0.0.1"
Port = 8080
#Now we bind the server instance to the host for connection to occur
server.bind(("", Port))
server.listen(5)
while True:
    c, addr = server.accept()
    print("connected to", addr)
    message = ("Thanking you for connecting")
    c.send(message.encode())
    c.close()
