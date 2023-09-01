import requests
import re
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
blue = Fore.BLUE
cyan = Fore.CYAN
background = white + green

def email_extractor(domain, google, name, saved_name):
    headers = {
        'User-Agent': 'Your User-Agent String',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/',
    }

    unique_emails = set()  # Set to store unique email addresses

    try:
        if domain.startswith('@'):
            query = f'{google} {name} + "{domain}"'
            print("Query:", query)
            response = requests.get(query, headers=headers)
            response.raise_for_status()  # Raise an exception if the response status code is not 200

            text = response.text
            emailreg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

            # finding matcjhing email with regex
            email_found = re.findall(emailreg, text)

            if email_found:
                print(blue + "Emails found:")
                for email in email_found:
                    if email not in unique_emails:
                        unique_emails.add(email)
                        print(background + email)
                        with open(saved_name, 'a') as email_file:
                            email_file.write(email + '\n')
            else:
                print(red + "No emails found on the page.")
                
        elif not domain.startswith('@'):
            print(red + 'Domain must start with @')
            import sys
            sys.exit()
            
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
    except Exception as e:
        print("Error:", e)


domain_name = input(cyan + "Enter domain name (e.g., @example.com): ")
while not domain_name.startswith('@'):
    print(red + 'Domain must start with @')
    domain_name = input(cyan + "Enter domain name (e.g., @example.com): ")
    
names_file_path = input(cyan + "Enter the path to the .txt file containing names: ")
saved_name = input('Enter name to Saved the Scraped email: ')

try:
    with open(names_file_path, "r") as file:
        for line in file:
            name = line.strip() 
            email_extractor(domain_name, "https://www.google.com/search?q=", name, saved_name)
except FileNotFoundError:
    print(red + "File not found.")
