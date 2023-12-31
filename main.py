import pyfiglet
import os
from colorama import Fore
from change_mac import change_mac
from scan_network import scan_network
from arp_spoof import arp_spoof
from dns_spoof import dns_spoof
from pkt_sniff import pkt_sniff
from port_scan import port_scan
from guess_passwrd import guess_passwrd
from crawl import subdomain_crawl, subdirectory_crawl, links_crawl

# Version

version = Fore.YELLOW + "v1.0" + Fore.WHITE


# System Functions

def exit_program():
    print(f"\n[+] Bye!")
    exit(0)


# Banner

def banner():
    os.system('clear')
    print(pyfiglet.figlet_format(f"R3CON SU!T3", font='slant'))


banner()

# Welcome

attack_types = [Fore.CYAN + "Network" + Fore.WHITE, Fore.GREEN + "Web Application" + Fore.WHITE]

print(f"[+] Welcome to Recon Suite {version} by Umar Ali")
print()
print(f"[1] {attack_types[0]} Assessment and Attacks")
print(f"[2] {attack_types[1]} Assessment and Attacks")
print(f"[3] Exit")
print()

try:
    choice = int(input("[.] $ "))
except KeyboardInterrupt:
    exit_program()

if choice == 1:
    banner()
    print("[1] Change MAC address")
    print("[2] Scan network for connected clients")
    print("[3] Execute ARP spoofing")
    print("[4] Execute DNS spoofing")
    print("[5] Initiate packet sniffing")
    print("[6] Scan for open ports")
    print("[7] Exit")
    print()
    choice = int(input(f"[./{attack_types[choice - 1]}] $ "))
    try:
        match choice:
            case 1:
                change_mac()
            case 2:
                scan_network()
            case 3:
                arp_spoof()
            case 4:
                dns_spoof()
            case 5:
                pkt_sniff()
            case 6:
                port_scan()
            case _:
                exit_program()
    except KeyboardInterrupt as ex:
        exit_program()
elif choice == 2:
    banner()
    print("[1] Guess login information of website")
    print("[2] Crawl page for hidden subdomains")
    print("[3] Crawl page for hidden subdirectories")
    print("[4] Find links in a webpage")
    print("[5] Exit")
    print()
    choice = int(input(f"[./{attack_types[choice - 1]}] $ "))
    try:
        match choice:
            case 1:
                guess_passwrd()
            case 2:
                subdomain_crawl()
            case 3:
                subdirectory_crawl()
            case 4:
                links_crawl()
            case 5:
                exit_program()
    except KeyboardInterrupt or ValueError:
        exit_program()
elif choice == 3:
    exit_program()
else:
    print("[!] Invalid Key. Exiting Program...")
