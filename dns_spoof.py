import time
from subprocess import call


def dns_spoof():
    """Spoofs links to initiate traffic redirection."""
    call("clear")
    print()
    original_link = input('Original Website/Link > ')
    spoof_link = input('Spoof Link/IP > ')
    print()
    print(f"$ python ./tools/dns_spoofer.py -l {original_link} -s {spoof_link}")
    print()
    try:
        call(f"python ./tools/dns_spoofer.py -l {original_link} -s {spoof_link}", shell=True)
    except KeyboardInterrupt:
        time.sleep(1)
