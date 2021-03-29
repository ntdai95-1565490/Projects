**Echo Client:**

1. Checks for valid command-line arguments
2. For each line of the user entered text, it creates a client socket and connects to the server with the user entered server IP address and port number
3. Encodes sending/Decodes receiving messages in UTF-8 format
4. Capped the size of the accepted client messages at 8192 bytes
5. STDOUT the same message received back from the server
6. Ends client process and exit the program, if the user hit ctrl - c (keyboard interrupt)

**Echo Server:**

1. Checks for valid command-line arguments
2. Creates a server socket with the user entered server port number
3. Accepts sockets from multiple clients
4. Encodes sending/Decodes receiving messages in UTF-8 format
5. Capped the size of the accepted client messages at 8192 bytes
6. STDOUT the message received from the client
7. Send the received messages back to their clients upon each request
8. Handle multiple request without terminating, but close down each client request after the task is performed

**Things to consider/improve:**

- Client currently can only send messages that are capped at 8192 bytes
- Printing out the messages and the IP address of clients that the message from to the server
- Currently, the only way to end the client process is with Keyboard interrupt with Ctrl - C