import time
import socket
import threading

def handle_client_connection(conn, addr):
    s_name = conn.recv(1024).decode()
    print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
    conn.send(name.encode())

    while True:
        message = conn.recv(1024).decode()
        print(s_name, ":", message)
        if message == "[e]":
            message = "Left chat room!"
            conn.send(message.encode())
            print("\n")
            break
        message = input(str("Me : "))
        conn.send(message.encode())

    conn.close()

print("\nWelcome to Chat Room\n")
print("Initializing....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))

s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

threading.Thread(target=handle_client_connection, args=(conn, addr)).start()
