import argparse
import socket
from contextlib import closing


DEFAULT_PORTS = (22, 80, 443, 3306)


def get_local_address():
    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "127.0.0.1"

    return hostname, ip_address


def check_port(host, port, timeout=1.0):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0


def scan_ports(host, ports=DEFAULT_PORTS, timeout=1.0):
    return [
        {"host": host, "port": port, "open": check_port(host, port, timeout)}
        for port in ports
    ]


def parse_ports(value):
    ports = []

    for raw_port in value.split(","):
        port = int(raw_port.strip())
        if port < 1 or port > 65535:
            raise argparse.ArgumentTypeError("ports must be between 1 and 65535")
        ports.append(port)

    return tuple(ports)


def build_parser():
    parser = argparse.ArgumentParser(description="Scan common TCP ports on a host.")
    parser.add_argument("--host", help="Host or IP address to scan. Defaults to local IP.")
    parser.add_argument("--ports", type=parse_ports, default=DEFAULT_PORTS, help="Comma-separated TCP ports.")
    parser.add_argument("--timeout", type=float, default=1.0, help="Connection timeout in seconds.")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    hostname, local_ip = get_local_address()
    host = args.host or local_ip

    print("NetWatch Scanner Initialized")
    print(f"Hostname: {hostname}")
    print(f"Target IP: {host}")

    for result in scan_ports(host, args.ports, args.timeout):
        status = "open" if result["open"] else "closed"
        print(f"Port {result['port']} is {status}")


if __name__ == "__main__":
    main()
