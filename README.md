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

Scan a single JS URL with output and save keys
python3 api_key_finder.py -u <url> -e

Scan a list of URLs silently (save keys only)
python3 api_key_finder.py -l <file.txt> -e --silence

## Requirements
Python 3

# Bought me a coffee 😇
## Bitcoin BTC Network
1G8tWgr1uwraMiG3X3bHwZFg8VNiWhcR74


## License
MIT License
