import argparse
import ipaddress
import socket


def resolve_host(ip_address):
    try:
        return socket.gethostbyaddr(str(ip_address))[0]
    except (socket.herror, socket.gaierror):
        return None


def scan_subnet(cidr, limit=None):
    network = ipaddress.ip_network(cidr, strict=False)
    results = []

    for index, ip_address in enumerate(network.hosts(), start=1):
        if limit is not None and index > limit:
            break

        results.append({"ip": str(ip_address), "hostname": resolve_host(ip_address)})

    return results


def build_parser():
    parser = argparse.ArgumentParser(description="Resolve hostnames on a subnet.")
    parser.add_argument("cidr", nargs="?", default="192.168.1.0/24", help="Subnet in CIDR notation.")
    parser.add_argument("--limit", type=int, default=20, help="Maximum hosts to scan.")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.limit < 1:
        raise SystemExit("--limit must be greater than zero")

    print(f"Scanning subnet {args.cidr}...")

    for result in scan_subnet(args.cidr, args.limit):
        hostname = result["hostname"] or "No hostname found"
        print(f"{result['ip']} -> {hostname}")


if __name__ == "__main__":
    main()
