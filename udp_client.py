import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 5000)

try:
    message = input("Enter a message: ").strip()

    if not message:
        print("Message cannot be empty.")
    else:
        client_socket.settimeout(5)

        client_socket.sendto(message.encode(), server_address)

        data, server = client_socket.recvfrom(1024)

        print("Server replied:", data.decode())

except socket.timeout:
    print("No response from the server within 5 seconds.")

except OSError as error:
    print("Network error:", error)

finally:
    client_socket.close()