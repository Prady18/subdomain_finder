import os
import subprocess
import whois


# Function to generate banner
def generate_banner():
    banner = r"""
 __   __  ___  ___  ___  ___  _   _ 
 \ \ / / / _ \ |  \/  | / _ \/ __|| | | |
  \ V / / /\ \| |\/| |/ /_\ \_ \| | | |
   \ /  |  _  || |  | ||  _  /|__) | |_| |
   \_/   \_| |_/\_|  |_/\_| \_/____/ \___/ 

       Subdomain Scanner with Information Gathering
           Author: Hacker01p
          GitHub: https://github.com/hacker01p
          Twitter: https://twitter.com/hacker01p
    """
    print(banner)


# Function to save subdomains to a file
def save_subdomains_to_file(subdomains):
    with open('subdomains.txt', 'w') as file:
        for subdomain in subdomains:
            file.write(subdomain + '\n')
    print('[+] Subdomains saved to subdomains.txt file.')


# Function to save domain information to a file
def save_domain_info_to_file(domain, info):
    with open('domain_info.txt', 'w') as file:
        file.write('Domain: {}\n'.format(domain))
        file.write('Registrar: {}\n'.format(info.registrar))
        file.write('Creation Date: {}\n'.format(info.creation_date))
        file.write('Expiration Date: {}\n'.format(info.expiration_date))
        file.write('Name Servers: {}\n'.format(info.name_servers))
    print('[+] Domain information saved to domain_info.txt file.')


# Main function
def main():
    generate_banner()
    domain = input('Enter the domain name: ')

    # Run sublist3r
    print('[+] Running sublist3r...')
    subprocess.run(['sublist3r', '-d', domain, '-o', 'subdomains.txt'])

    # Save subdomains to a file
    with open('subdomains.txt', 'r') as file:
        subdomains = [line.strip() for line in file]
    save_subdomains_to_file(subdomains)

    # Fetch domain information using whois
    print('[+] Fetching domain information...')
    info = whois.whois(domain)

    # Save domain information to a file
    save_domain_info_to_file(domain, info)

    print('[+] Information Gathering Completed!')


