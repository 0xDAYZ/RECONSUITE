#!/usr/bin/env python
import optparse
from datetime import datetime
import socket
from prettytable import PrettyTable
from colorama import Fore


def scan_for_ports(target):
    open_ports = []
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        # print(port)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)

    return open_ports


def get_protocol(port):
    protocols = {
        20: 'FTP',
        21: 'FTP',
        22: 'SSH',
        25: 'Legacy SMTP',
        53: 'DNS',
        80: 'HTTP',
        123: 'NTP',
        135: 'RPC',
        139: 'NetBIOS',
        179: 'BGP',
        443: 'HTTPS',
        445: 'SMB',
        500: 'ISAKMP',
        587: 'Modern SMTP',
        3389: 'RDP',
        6666: 'Possible Backdoor'
    }

    if port in protocols:
        return protocols[port]
    else:
        return 'Unknown'


def show_ports(open_ports):
    formatted_ports = []
    for port in open_ports:
        formatted_ports.append([port, get_protocol(port)])

    table = PrettyTable()
    table.field_names = [Fore.BLUE + "Port Open" + Fore.WHITE, Fore.YELLOW + "Protocol" + Fore.WHITE]

    for item in formatted_ports:
        table.add_row(item)
    table.add_autoindex(Fore.CYAN + "" + Fore.WHITE)
    table.hrules = True
    print()

    print(table)


def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-t', '--target', dest='scan_target', help="Target IP to Scan.")
    (option, argument) = parser.parse_args()

    if not option.scan_target:
        parser.error("[!] Target IP expected. Try --help for more info.")
    return option


opt = get_options()

try:
    print("#" * 48)
    print(f"[+] Scanning {Fore.LIGHTCYAN_EX + opt.scan_target + Fore.WHITE}")
    print(
        f'[+] Scan started at: {Fore.LIGHTGREEN_EX + str(datetime.now().strftime("%b %d, %Y @ %I:%M %p %Z")) + Fore.WHITE}')
    print("#" * 48)

    res = scan_for_ports(opt.scan_target)
    show_ports(res)
    print()
    print(Fore.LIGHTRED_EX + "[x] End of Scan." + Fore.WHITE)
except KeyboardInterrupt:
    print()
    print(Fore.LIGHTRED_EX + "[x] Scan terminated unexpectedly." + Fore.WHITE)
