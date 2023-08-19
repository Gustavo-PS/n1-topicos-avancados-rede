from socket import *

def caesar_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_char = chr((ord(char) - shift) % 256)
        decrypted_message += decrypted_char
    return decrypted_message

serverPort = 15600
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("UDP server\n")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    encrypted_text = str(message, "utf-8")
    
    shift = 5  # Shift correspondente à cifra de César
    
    decrypted_message = caesar_decrypt(encrypted_text, shift)
    print("Mensagem decriptografada:", decrypted_message)
