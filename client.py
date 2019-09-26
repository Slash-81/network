import socket

HOST = "192.168.4.182"
PORT = 5000

user = input("Enter login>>")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect((HOST, PORT))
client.send(user.encode("utf-8"))

while True:
    message = input("Enter your message>>")
    data = f"User:{user}\r\n{message}\n"
    try:
        client.send(data.encode("utf-8"))
    except Exception as e:
        print(e)
    request = client.recv(2048)
    print(request.decode("utf-8"))