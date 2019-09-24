import socket

HOST = "127.0.0.1"
PORT = 5000

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind((HOST, PORT))
srv.listen(20)
try:

    client, addr = srv.accept()
    for index in range(1, 10):
        data = client.recv(2048)
        print(data.decode("utf-8"))
        if not data:
            break
        result = f"{data}\n{addr}\n"
        client.send(data)
except Exeption as e:
    print(e)
finally:
    srv.close()
