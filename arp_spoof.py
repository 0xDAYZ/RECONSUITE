import time
from subprocess import call


def arp_spoof():
    """Spoofs two devices together to introduce MITM."""
    call("clear")
    print()
    target_1 = input('Target 1 > ')
    target_2 = input('Target 2 > ')
    print()
    print(f"$ python3 ./tools/arp_spoofer.py -a {target_1} -b {target_2}")
    print()
    try:
        call(f"python3 ./tools/arp_spoofer.py -a {target_1} -b {target_2}", shell=True)
    except KeyboardInterrupt:
        time.sleep(1)
