import socket
server = socket.socket()
server.bind(("localhost",9999))
server.listen(1)
print("server listing")
conn,addr = server.accept()
print("connect with:",addr)

msg = conn.recv(1024).decode()
print('client',msg)
conn.send("Hello".encode())
conn.close()