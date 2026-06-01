import socket

print('NetWatch Scanner Initialized')

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f'Hostname: {hostname}')
print(f'Local IP: {ip_address}')
