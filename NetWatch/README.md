# NetWatch

NetWatch provides small, explicit CLI utilities for local network diagnostics.

## Port scan

```bash
python scanner.py --host 127.0.0.1 --ports 22,80,443 --timeout 1
```

## Subnet hostname scan

```bash
python subnet_scan.py 192.168.1.0/24 --limit 20
```

Use these tools only on networks you own or have permission to assess.
