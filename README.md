## ⚠️ Disclaimer
This tool is intended for ethical security testing only. Do not use it for unauthorized or illegal activities. ⚠️

## API Key Finder 🔑
API Key Finder is a lightweight Python tool designed to scan JavaScript files (via URLs or lists of URLs) and extract sensitive API keys and secrets automatically.

## Features
Scan a single JavaScript URL or multiple URLs from a file.

Detects a variety of common API keys including:

Twilio SIDs

Heroku API Keys

Square Access Tokens

Stripe Secret Keys

AWS Access Keys

Google API Keys

Slack Tokens

SendGrid API Keys

GitHub Tokens

And more...

Save discovered keys into separate files per key type.

Optional silent mode (--silence) to save keys without printing to console.

Simple command-line interface with clear options.

Built with Python using requests and regex for fast scanning.

Usage
bash
Copy
Edit

## 📦 Installation
### bash
```
git clone https://github.com/Red-Eye999/api_key_finder
cd api_key_finder
chmod +x api_key_finder.py
pip install -r requirements.txt
```
### scanning single a URL
Scan a single JS URL with output and save keys in text files
```
python3 api_key_finder.py -u <url> -e
```
Scan a single of URL silently (save keys only)
```
python3 api_key_finder.py -u <url> -e --silence
```
Scan a single JS URL with output only
```
python3 api_key_finder.py -u <url>
```
### scanning multiple JS URLs
Scan a list JS URLs with output and save keys in text files
```
python3 api_key_finder.py -l <TEXT_FILE.txt> -e
```
Scan a list JS URLs silently (save keys only)
```
python3 api_key_finder.py -l <TEXT_FILE.txt> -e --silence
```
Scan a list JS URLs with output only
```
python3 api_key_finder.py -l <TEXT_FILE.txt>
```

## Requirements
Python 3

# Bought me a coffee 😇
### Bitcoin BTC Network
1G8tWgr1uwraMiG3X3bHwZFg8VNiWhcR74


## License
MIT License
