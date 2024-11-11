import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(1)
print("سرور آماده و در حال گوش دادن...")

client_socket, client_address = server_socket.accept()
print(f"ارتباط با {client_address} برقرار شد.")

while True:
    message = client_socket.recv(1024).decode()
    if message.lower() == "exit":
        print("ارتباط با کلاینت خاتمه یافت.")
        break
    print(f"کلاینت: {message}")

    response = input("سرور: ")
    client_socket.send(response.encode())
    if response.lower() == "exit":
        print("ارتباط توسط سرور خاتمه یافت.")
        break

client_socket.close()
server_socket.close()
