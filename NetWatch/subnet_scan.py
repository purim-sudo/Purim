import socket

base_ip = '192.168.1.'

print('Scanning subnet...')

for i in range(1, 10):
    ip = base_ip + str(i)

    try:
        hostname = socket.gethostbyaddr(ip)
        print(f'{ip} -> {hostname[0]}')
    except:
        print(f'{ip} -> No hostname found')
