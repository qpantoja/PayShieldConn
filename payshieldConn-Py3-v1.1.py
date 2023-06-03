###############################################################################################
# Quetzalcoatl Pantoja H.
# Date: 2023-05-16
# Version 1.0
# Python v3
# Description: Connect to PayShield through TLS/TCP
###############################################################################################

import socket
import ssl
import sys

# Define the IP address and port number of the PayShield device
ip_address = 'XX.XX.XX.XX'
port = 2500

# Encode a command to be sent to PayShield
def encode_str(command_dec):
    length = len(command_dec)
    command_enc = bytearray([0]) + length.to_bytes(1, 'big') + command_dec.encode()
    return command_enc

# Decode a command received from PayShield
def decode_str(response_enc):
    response_dec = response_enc.decode()
    return response_dec

# Get the command from the user input
if len(sys.argv) < 2:
    print('Usage: python payshield.py [command]')
    sys.exit(1)
command_str = sys.argv[1]
command = encode_str(command_str)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL/TLS support
client_context = ssl.create_default_context()
client_socket = client_context.wrap_socket(client_socket, server_hostname=ip_address)

# Connect to the PayShield device
try:
    client_socket.connect((ip_address, port))
except socket.error as e:
    print(f'Error: Could not connect to PayShield device ({e}).')
    sys.exit(1)

# Send the command to the PayShield device
try:
    client_socket.sendall(command)
except socket.error as e:
    print(f'Error: Could not send command to PayShield device ({e}).')
    sys.exit(1)

# Receive the response from the PayShield device
response = client_socket.recv(1024)

response_str = decode_str(response)

# Print the response
print(response_str)

# Close the socket connection
client_socket.close()
