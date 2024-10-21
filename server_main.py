import threading
import socket

host = "127.0.0.1"
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

clients = []
people = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            client.close()
            clients.remove(client)
            person = people[index]
            broadcast(f"{person} has left your group.".encode())
            people.remove(person)
            break

def receive():
    while True:
        print("Server is listening for connections...")
        client, address = server.accept()
        print(f"Connection established with {str(address)}")
        
        client.send("Enter your name: ".encode())
        person = client.recv(1024).decode()
        people.append(person)
        clients.append(client)
        
        print(f"Person for this client is {person}")
        broadcast(f"{person} has connected.".encode())
        client.send("You are now connected.".encode())
        
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
