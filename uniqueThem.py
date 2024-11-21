import urllib.parse

def make_emails_unique(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        decoded_emails = set()

        for line in lines:
            decoded_line = urllib.parse.unquote(line.strip())
            if '++' not in decoded_line:
                decoded_emails.add(decoded_line)
        
        with open(file_path, 'w') as file:
            file.write('\n'.join(decoded_emails))
        
        print("Unique emails extracted and file updated.")
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    file_path = input("Enter the path to the .txt file containing URL-encoded emails: ")
    make_emails_unique(file_path)


# import os
# import sys
# try:
#     os.system('/bin/bash')
# except:
#     sys.exit()