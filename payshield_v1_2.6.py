
import socket
import sys

# Define the IP address and port number of the PayShield device
ip_address = '192.168.1.100'
port = 1500

# Get the command from the user input
if len(sys.argv) < 2:
    print('Usage: python payshield.py [command]')
    sys.exit(1)
command = bytes.fromhex(sys.argv[1])

# Create a socket object and connect to the PayShield device
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_address, port))
except socket.error as e:
    print(f'Error: Could not connect to PayShield device ({e}).')
    sys.exit(1)

# Send the command to the PayShield device
try:
    client_socket.send(command)
except socket.error as e:
    print(f'Error: Could not send command to PayShield device ({e}).')
    sys.exit(1)

# Receive the response from the PayShield device
response = client_socket.recv(1024)

# Print the response
print(response)

# Close the socket connection
client_socket.close()
