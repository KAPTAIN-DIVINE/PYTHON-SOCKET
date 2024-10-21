import threading
import socket

person = input("Choose someone >>> ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "person?":
                client.send(person.encode())
            else:
                print(message)
        except:
            print("Error occurred.")
            client.close()
            break

def client_send():
    while True:
        message = f"{person}: {input('')}"    
        client.send(message.encode())

receive_thread = threading.Thread(target=client_receive)  
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
