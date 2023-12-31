#!/usr/bin/env python
import optparse
import re
import subprocess
import scapy.all as scapy
from prettytable import PrettyTable
from colorama import Fore


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request

    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    response = []

    for client in answered:
        ip = client[1].psrc
        mac = client[1].hwsrc
        response.append([ip, mac])

    return response


def get_system_info():
    result = subprocess.check_output(['ifconfig', 'eth0'])
    mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', result.decode())
    ip = re.search(r'\d+.\d+.\d+.\d+', result.decode())
    return mac.group(0), ip.group(0)


def print_scan_result(response):
    table = PrettyTable()
    table_system_details = PrettyTable()

    table.field_names = [Fore.MAGENTA + "IP Address" + Fore.WHITE, Fore.YELLOW + "MAC Address" + Fore.WHITE]
    for item in response:
        table.add_row(item)
    table.add_autoindex(Fore.CYAN + "Device" + Fore.WHITE)
    table.hrules = True
    print()

    table_system_details.add_row([Fore.LIGHTRED_EX + "System MAC" + Fore.WHITE, Fore.LIGHTGREEN_EX + f"{get_system_info()[0]}" + Fore.WHITE])
    table_system_details.add_row([Fore.LIGHTRED_EX + "System IP" + Fore.WHITE, Fore.LIGHTGREEN_EX + f"{get_system_info()[1]}" + Fore.WHITE])
    table_system_details.header = False
    table_system_details.hrules = True
    print('#' * 48)
    print(table_system_details)
    print('#' * 48)
    print(table)


def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--target', dest='target', help="Target IP/Range.")
    (option, argument) = parser.parse_args()

    if not option.target:
        parser.error("[!] Target expected. Try --help for more info.")

    return option


opt = get_options()
scan_result = scan(opt.target)
print_scan_result(scan_result)
