import socket

client = socket.socket()
client.connect(("localhost",9999))
client.send("Hi this is".encode())
msg = client.recv(1024).decode()
print("server:",msg)
client.close()