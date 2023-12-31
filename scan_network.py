from subprocess import call


def scan_network():
    """Scans the network for all connected clients."""
    call("clear")
    print()
    ip_target = input('IP > ')
    print()
    print(f"$ python3 ./tools/network_scanner.py -t {ip_target}")
    print()
    call(f"python3 ./tools/network_scanner.py -t {ip_target}", shell=True)
