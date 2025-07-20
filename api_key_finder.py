import re
import requests
import sys
import os

regex_patterns = {
    "Twilio SID": r"AC[a-zA-Z0-9]{32}",
    "Twilio Auth Token": r"SK[a-zA-Z0-9]{32}",
    "Heroku API Key": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
    "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
    "Amazon AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
    "Stripe Live Secret Key": r"sk_live_[0-9a-zA-Z]{24}",
    "Square Access Token": r"EAAA[0-9A-Za-z\-_]{20,}",
    "Basic Auth in URL": r"[a-zA-Z0-9\-_]+:[a-zA-Z0-9\-_]+@"
}

def save_key(name, key):
    if name == "Twilio SID":
        filename = "twilio-sid.txt"
    elif name == "Heroku API Key":
        filename = "heroku-api.txt"
    elif name == "Square Access Token":
        filename = "access-token.txt"
    else:
        return  
    
    with open(filename, "a") as f:
        f.write(key + "\n")

def scan_content(source, content, extract=False, silence=False):
    found = []
    for name, pattern in regex_patterns.items():
        matches = re.findall(pattern, content)
        for match in matches:
            found.append((name, match))
            if extract:
                save_key(name, match)
    if found and not silence:
        print(f"\n[ + ] Results from: {source}")
        for name, match in found:
            print(f"{name:30} -> {match}")
    elif not found and not silence:
        print(f"[ - ] No secrets found in: {source}")

def scan_url(url, extract=False, silence=False):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            scan_content(url, response.text, extract=extract, silence=silence)
        else:
            if not silence:
                print(f"[!] Failed to fetch {url} - Status code: {response.status_code}")
    except Exception as e:
        if not silence:
            print(f"[!] Error fetching {url}: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python3 api_key_finder.py -l <js_links.txt> [-e] [--silence]   # list of URLs")
        print("  python3 api_key_finder.py -u <url> [-e] [--silence]            # single JS file URL")
        sys.exit(1)

    option = sys.argv[1]
    target = sys.argv[2]

    extract = "-e" in sys.argv
    silence = "--silence" in sys.argv

    if option == "-u":
        scan_url(target, extract=extract, silence=silence)
    elif option == "-l":
        if not os.path.isfile(target):
            print(f"[!] File not found: {target}")
            sys.exit(1)
        with open(target, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
            for url in urls:
                scan_url(url, extract=extract, silence=silence)
    else:
        print("[!] Unknown option. Use -u for URL or -l for list file.")

if __name__ == "__main__":
    main()
