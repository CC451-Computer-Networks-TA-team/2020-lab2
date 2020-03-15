import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ("127.0.0.1", 54444)
# New!, TCP is a stream protocol; it needs
# to be connected first.
client_socket.connect(server_addr)

client_socket.send(b"Hello!")

# Note, this will work only once if you're
# using the sample tcp_server.
# But you can use netcat to make a TCP server
# that won't shutdown on its own.
while True:
    msg = input("Enter: ")
    client_socket.send(msg.encode())

    if msg == "ex":
        break
client_socket.close()
