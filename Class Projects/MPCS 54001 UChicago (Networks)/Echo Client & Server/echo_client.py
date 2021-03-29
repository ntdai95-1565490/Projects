# Importing socket, re and sys (for command-line arguments) modules
from socket import *
from sys import *
from re import *

class EchoClient:
    def __init__(self):
        # Checking if the user entered only two command-line arguments, which is the server's IP address and the port number
        if len(argv) != 3:
            print("Please, enter the server ip address and port number in the command-line arguments only.")
        # Checking if the user entered a valid IP address for the server using regular expression
        elif match("[0-9.]+$", argv[1]) == None:
            print("Please, enter a valid IP address for the server.")
        # Checking if the user entered a valid server port number between 1024 and 65535, inclusive
        elif argv[2].isnumeric() and 1024 <= int(argv[2]) <= 65535:
            # Initializing the user entered server IP address, port number from the command-line and the server address
            self.echo_server_hostname = str(argv[1])
            self.echo_server_port_number = int(argv[2])
            self.echo_server_address = (self.echo_server_hostname, self.echo_server_port_number)
            # Initializing the encoding/decoding format of the texts and delimiting the size of messages to 8192 bytes
            self.format = "utf-8"
            self.network_buffer_size = 8192
            # Running the client if the user entered valid server ip address and port number
            self.echo_client_run()
        # If the user didn't entered a valid server port number, print out the warning message
        else:
            print("Please, enter a valid server port number between 1024 and 65535, inclusive.")

    def echo_client_run(self):
        try:
            # For each text line that the user entered, create a socket, connect to the server, encode the text and send to the server,
            # and then print out the received text back to the client
            for echo_client_text_line in stdin:
                self.echo_client_TCP_socket = socket(AF_INET, SOCK_STREAM)
                self.echo_client_TCP_socket.connect(self.echo_server_address)
                self.echo_client_TCP_socket.send(echo_client_text_line.encode(self.format))
                echo_client_text_line_back = self.echo_client_TCP_socket.recv(self.network_buffer_size).decode(self.format)
                stdout.write(f"Text received back from the server: {echo_client_text_line_back}")
        # If the user presses ctrl-c, end the client process and exit (sys) the program
        except KeyboardInterrupt:
            stdout.write("Echo client process ended.")
            exit()

if __name__ == "__main__":
    EchoClient()