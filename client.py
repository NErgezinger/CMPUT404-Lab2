import socket

s = socket.socket()

s.connect(('www.google.com', 80))
s.sendall(b'GET / HTTP/1.1 \r\nHost: www.google.com\r\n\r\n')

s.settimeout(.2)
all_data = b''
while True:
    data = s.recv(1024)
    if not data: break
    all_data += data

print(all_data)
s.close()