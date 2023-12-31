#!/usr/bin/env python
import subprocess
import optparse
import re
from colorama import Fore
import time


def animation_print(interface, new_mac_address):
    print(f'\r[+] Changing MAC address of {interface} to {new_mac_address}..' + '|', end='')
    time.sleep(0.5)
    print(f'\r[+] Changing MAC address of {interface} to {new_mac_address}...' + '/', end='')
    time.sleep(0.5)
    print(f'\r[+] Changing MAC address of {interface} to {new_mac_address}....' + '-', end='')
    time.sleep(0.5)
    print(f'\r[+] Changing MAC address of {interface} to {new_mac_address}.....' + '\\', end='')
    time.sleep(0.5)
    print(f'\r[+] Changing MAC address of {interface} to {new_mac_address}......' + '|', end='')
    time.sleep(0.5)
    print(f'\r[+] Changing MAC address of {interface} to {new_mac_address}.......' + '/', end='')
    time.sleep(0.5)
    print(f'\r[+] Changing MAC address of {interface} to {new_mac_address}........' + '-', end='')
    time.sleep(0.5)
    print(f'\r[+] Changing MAC address of {interface} to {new_mac_address}.........' + '\\', end='')
    time.sleep(0.5)
    print(f'\r[+] Changing MAC address of {interface} to {new_mac_address}..........' + '|', end='')
    time.sleep(0.5)
    print(f'\r[+] Changing MAC address of {interface} to {new_mac_address}           ', end='')


def change_mac(interface, new_mac_address):
    subprocess.call(['ifconfig', interface, 'down'])
    animation_print(interface, new_mac_address)
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac_address])
    subprocess.call(['ifconfig', interface, 'up'])


def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help="Interface to change.")
    parser.add_option('-M', '--mac', dest='new_mac_address', help="New MAC address.")
    (option, argument) = parser.parse_args()

    if not option.interface:
        parser.error("[!] Interface expected. Try --help for more info.")
    if not option.new_mac_address:
        parser.error("[!] MAC address expected. Try --help for more info.")

    return option


def current_mac(interface):
    result = subprocess.check_output(['ifconfig', interface])
    formatted_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', result.decode())
    if formatted_result:
        return formatted_result.group(0)
    else:
        print('[-] Could not read MAC address.')


opt = get_options()
print(f'[+] Current MAC Address: {Fore.YELLOW + str(current_mac(opt.interface)) + Fore.WHITE}')
print()
change_mac(opt.interface, opt.new_mac_address)
print()
print(f'\n[+] New MAC Address: {Fore.GREEN + str(current_mac(opt.interface)) + Fore.WHITE}')
