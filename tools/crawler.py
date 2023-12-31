#!/usr/bin/env python
import optparse
from os import path
from colorama import Fore
import requests
import re
import urllib.parse


def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-u', '--url', dest='url', help="URL of Target")
    parser.add_option('-f', '--function', dest='function', help="Target Webpage")
    (option, argument) = parser.parse_args()

    return option


def request(url):
    try:
        response = requests.get("http://" + url)
        if response.status_code == 200:
            return response
        else:
            return None
    except requests.exceptions.ConnectionError:
        return None


def crawl_for_subdirectories(url):
    file_location = path.abspath("./ReconSuitev1/tools/subdirectories.txt")
    try:
        with open(file_location, 'r') as wordlist:
            for item in wordlist:
                test_url = f"{url}/{item.strip()}"
                response = request(test_url)
                if response is not None:
                    print("[+] " + Fore.LIGHTGREEN_EX + f"http://{test_url + Fore.WHITE} exists.")
    except KeyboardInterrupt:
        print("\n[x] Exiting Crawler...")


def crawl_for_subdomains(url):
    file_location = path.abspath("./ReconSuitev1/tools/subdomains.txt")
    try:
        with open(file_location, 'r') as wordlist:
            for subdomain in wordlist:
                test_url = f"{subdomain.strip()}.{url}"
                response = request(test_url)
                if response is not None:
                    print("[+] " + Fore.LIGHTGREEN_EX + f"http://{test_url + Fore.WHITE} exists.")
    except KeyboardInterrupt:
        print("\n[x] Exiting Crawler...")


def show_embed_links(url):
    response = request(url)
    href_links = re.findall('(?:href=")(.*?)"', str(response.content))

    for link in href_links:
        link = "http://" + urllib.parse.urljoin(url, link)
        print(f"[+] {link}")


opt = get_options()

match opt.function.lower():
    case "crawl_for_subdirectories":
        crawl_for_subdirectories(opt.url)
    case "crawl_for_subdomains":
        crawl_for_subdomains(opt.url)
    case "show_embed_links":
        show_embed_links(opt.url)
    case _:
        pass


