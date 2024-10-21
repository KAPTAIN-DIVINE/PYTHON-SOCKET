import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    client = int(input("Enter the number of clients: "))
    s.connect((host, port))

    while True:
        filename = input("Input filename: ")
        try:
            fi = open(filename, "r")
            data = fi.read()

            if not data:
                print("File is empty.")
                break

            while data:
                s.send(data.encode())
                data = fi.read()

            fi.close()

        except IOError:
            print("Enter a valid file name...")
        except Exception as e:
            print(f"An error occurred: {e}")
