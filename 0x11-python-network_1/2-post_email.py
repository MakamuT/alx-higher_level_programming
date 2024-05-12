#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body
"""
from sys import argv
import urllib.request
import urllib.parse

if __name__ == '__main__':
    if len(argv) != 3:
        print("Usage: ./script.py <url> <email>")
        sys.exit(1)

    url = argv[1]
    email = argv[2]

    DATA = urllib.parse.urlencode({"email": email}).encode('ascii')

    try:
        with urllib.request.urlopen(url, DATA) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Errir: {e.code} {e.reason}")
