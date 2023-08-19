from socket import *

def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        encrypted_char = chr((ord(char) + shift) % 256)
        encrypted_message += encrypted_char
    return encrypted_message

serverName = "127.0.0.1"  # IPv4 // ::1 IPv6
serverPort = 15600
clientSocket = socket(AF_INET, SOCK_DGRAM)  # AF_INET6
print("UDP Client\n")
while True:
    message = input("Input message: ")
    if message == "exit":
        break
    
    shift = 5  # Shift para a cifra de César
    
    encrypted_message = caesar_encrypt(message, shift)    
    clientSocket.sendto(bytes(encrypted_message, "utf-8"), (serverName, serverPort))

clientSocket.close()
