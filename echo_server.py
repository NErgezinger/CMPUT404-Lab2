import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 8001))
s.listen(1)

while True:
    conn, addr = s.accept()
    conn.settimeout(.2)
    print("Connection from", addr)

    all_data = b''
    while True:
        try:
            data = conn.recv(1024)
            all_data += data
        except socket.timeout:
            break
    
    print(all_data)
    conn.sendall(all_data)
    conn.shutdown(socket.SHUT_WR)
    conn.close()