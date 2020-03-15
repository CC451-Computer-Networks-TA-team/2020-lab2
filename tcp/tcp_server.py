import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ("127.0.0.1", 54444)
server_socket.bind(server_addr)

# New! TCP server doesn't work the same as UDP.
# the server socket (welcome socket) makes a new
# socket for each connecting client.
server_socket.listen(10)
print("Waiting for clients...")

# New! accept() receives a TCP client
# now the connection on the client side
# is established.
client_socket, client_addr = server_socket.accept()
client_socket.send(b"1234")  # Send a reply
client_socket.close()
