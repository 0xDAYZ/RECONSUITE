from subprocess import call


def change_mac():
    """ Changes the MAC Address of the current system."""
    call("clear")
    print()
    interface = input('Interface > ')
    new_mac = input('New MAC > ')
    print()
    print(f"$ python3 ./tools/mac_changer.py -i {interface} -M {new_mac}")
    print()
    call(f"python3 ./tools/mac_changer.py -i {interface} -M {new_mac}", shell=True)
