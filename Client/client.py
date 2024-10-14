import socket
def client():
    host = socket.gethostname()

    port = 21042

    client_socket = socket.socket()

    client_socket.connect((host, port))

    message = input("Enter your message (Type 'bye' to exit): ")

    while message.lower().strip() != "bye":
        # Send the message to the server
        client_socket.send(message.encode())
        # Receive a response from the server
        data = client_socket.recv(1024).decode()
        # Display the received message from the server
        print(f"Received from server:\033[92m {data} \033[0m" )
        # Prompt for the next message
        message = input("Enter your message (Type 'bye' to exit): ")
    # Close the connection
    client_socket.close()


if __name__ == "__main__":
    client()
