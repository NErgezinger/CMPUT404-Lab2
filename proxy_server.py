import socket
from multiprocessing import Process

def get_google(s_conn):
    # print("Process starting")
    s_conn.settimeout(.5)
    all_client_data = b''
    while True:
        try:
            client_data = s_conn.recv(1024)
            all_client_data += client_data
        except socket.timeout:
            break
    
    # print("Received from client:", all_client_data)

    s_goog = socket.socket()
    s_goog.settimeout(.5)

    s_goog.connect(("www.google.com", 80))
    s_goog.sendall(all_client_data)
    all_goog_data = b''
    while True:
        try:
            goog_data = s_goog.recv(1024)
            all_goog_data += goog_data
        except socket.timeout:
            break
    
    s_conn.sendall(all_goog_data)
    s_conn.shutdown(socket.SHUT_WR)
    s_conn.close()

    s_goog.close()

    # print("Process finishing")

if __name__ == "__main__":
    s_serv = socket.socket()
    s_serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s_serv.bind(('', 8001))
    s_serv.listen(1)
    while True:
        conn, addr = s_serv.accept()
        p = Process(target=get_google, args=(conn,))
        p.start()