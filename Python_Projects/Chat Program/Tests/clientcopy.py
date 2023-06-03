import time
import socket
import threading

def receive_messages():
    while True:
        message = s.recv(1024).decode()
        print(s_name, ":", message)

def send_messages():
    while True:
        message = input(str("Me : "))
        s.send(message.encode())
        if message == "[e]":
            message = "Left chat room!"
            s.send(message.encode())
            print("\n")
            break

print("\nWelcome to Chat Room\n")
print("Initializing....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
port = 1234
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

name = input("Enter your name: ")
s.send(name.encode())
s_name = s.recv(1024).decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
