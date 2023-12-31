from subprocess import call


def port_scan():
    """Scans for all open ports of a given target."""
    call("clear")
    print()
    target = input('Target > ')
    print()
    print(f"$ python3 ./tools/port_scanner.py -t {target}")
    print()
    call(f"python3 ./tools/port_scanner.py -t {target}", shell=True)
