import socket

def server():
    try:
        host = socket.gethostname()

        port = 21042
        s = socket.socket()
        s.bind((host, port))
        s.listen(2)
        c, address = s.accept()
        print(f"Connected to: {address}")

        while True:
            data = c.recv(1024).decode()
            if not data:
                break
            print(f"Received from client: \033[92m {data}\033[0m")

            response = input("Enter response to send to client: ")
            c.send(response.encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        c.close()


if __name__ == "__main__":
    server()