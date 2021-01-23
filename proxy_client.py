import socket

s = socket.socket()

s.connect(('localhost', 8001))
s.sendall(b'GET / HTTP/1.1 \r\nhost: www.google.com\r\n\r\n')

all_data = b''
while True:
    data = s.recv(1024)
    if not data: break
    all_data += data

print(all_data)

s.shutdown(socket.SHUT_WR)
s.close()