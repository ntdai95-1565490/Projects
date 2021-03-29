# Importing socket and sys (for command-line arguments) modules
from socket import *
from sys import *

class EchoServer:
    def __init__(self):
        # Checking if the user entered only one command-line argument, which is the port number and if it's between 1024 and 65535,
        # inclusive
        if len(argv) == 2 and argv[1].isnumeric() and 1024 <= int(argv[1]) <= 65535:
            # Initializing the user entered server port number from the command-line and the server address
            self.echo_server_port_number = int(argv[1])
            self.echo_server_address = (gethostname(), self.echo_server_port_number)
            # Printing out the IP address of the server for the clients to connect
            print(f"The IP adress of the server is {gethostbyname(gethostname())}")
            # Initializing the encoding/decoding format of the texts and delimiting the size of messages to 8192 bytes
            self.format = "utf-8"
            self.network_buffer_size = 8192
            # Creating the server socket and run the server to listen to clients
            self.echo_server_TCP_socket = socket(AF_INET, SOCK_STREAM)
            self.echo_server_TCP_socket.bind(self.echo_server_address)
            self.echo_server_TCP_socket.listen(5)
            self.echo_server_run()
        else:
            print("Please, enter a valid server port number (between 1024 and 65535, inclusive) as the only command-line argument.")

    def echo_server_run(self):
        # Creating an infinite loop, so that a server can wait and listen for multiple client requests without terminating
        while True:
            # Accepting and decoding the text from the client
            (echo_client_TCP_socket, echo_client_address) = self.echo_server_TCP_socket.accept()
            echo_client_text_line = echo_client_TCP_socket.recv(self.network_buffer_size).decode(self.format)
            # Printing out the text in the server in STDOUT
            stdout.write(f"Text received from the client: {echo_client_text_line}")
            # Encoding and sending the message back to the client
            echo_client_TCP_socket.send(echo_client_text_line.encode(self.format))
            # Closing the socket after each client request
            echo_client_TCP_socket.close()

if __name__ == '__main__':
    EchoServer()