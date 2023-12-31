import time
from subprocess import call


def pkt_sniff():
    """Sniffs for data packets over an interface."""
    call("clear")
    print()
    interface = input('Interface > ')
    print()
    print(f"$ python3 ./tools/packet_sniffer.py -i {interface}")
    print()
    try:
        call(f"python3 ./tools/packet_sniffer.py -i {interface}", shell=True)
    except KeyboardInterrupt:
        time.sleep(1)
