import socket
import threading


HOST = "127.0.0.1"
PORT = 5000

def executor(socket_key):
    try:
        socket = storage[socket_key]
    except KeyError:
        print(f"Key{socket_key} not found")
        return
    try:
        while True:
            data = socket.recv(2048)
            response = data.decode("utf-8")
            
            if "close" in responce:
                break
            for client, client_socket in storage.items():
                if client !=socket_key:
                    print(client, responce)
                    client_socket.send(f"{client[0]}\n".encode("utf-8"))
                    client_socket.send(response.encode("utf-8"))
    except Exception as e:
        print(e)
    finally:
        socket.close()
        del storage[socket_key]

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((HOST, PORT))
srv.listen(20)
storage = {}

try:
    flag = True
    while flag:
        client, addr = srv.accept()
        storage[addr] = client
        worker = threading.Thread(target=executor, args=(addr,))
        worker.start()

except Exeption as e:
    print(e)
finally:
    srv.close()
