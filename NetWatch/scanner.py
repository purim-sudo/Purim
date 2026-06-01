import socket

print('NetWatch Scanner Initialized')

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f'Hostname: {hostname}')
print(f'Local IP: {ip_address}')

ports = [22, 80, 443, 3306]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip_address, port))

    if result == 0:
        print(f'Port {port} is open')
    else:
        print(f'Port {port} is closed')

    sock.close()
