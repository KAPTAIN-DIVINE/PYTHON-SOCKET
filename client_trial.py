import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("127.0.0.1", 8080))
print(server.recv(1024))
server.close()
