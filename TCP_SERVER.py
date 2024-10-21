import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if __name__ == "__main__":
    host ="127.0.0.1"
    port = 8080
    client = int(input("Enter the number of clients: "))
    s.bind((host, port))
    s.listen(client)
    connections = []
    print("Initialting the clients")
    
for i in range(client):
    conn = s.accept()
    connections.append(conn)
    print("connected with clients", i+1)
fileno = 0
idx = 0
for conn in connections:
    idx += 1
    data = conn[0].recv(1024).decode()
    if not data:
        continue
    filename = "output" + str(fileno) + ".txt"
    fo = open(filename, "W")
    while data:
        break
    else: 
        fo.write(data)
        data = conn[0].recv(1024).decode()
        print("received connection from", filename)
        for conn in connections:
            conn[0].close
            