import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

print("ارتباط با سرور برقرار شد. برای خروج 'exit' را تایپ کنید.")

while True:
    message = input("کلاینت: ")
    client_socket.send(message.encode())
    if message.lower() == "exit":
        print("ارتباط توسط کلاینت خاتمه یافت.")
        break

    response = client_socket.recv(1024).decode()
    if response.lower() == "exit":
        print("ارتباط توسط سرور خاتمه یافت.")
        break
    print(f"سرور: {response}")

client_socket.close()