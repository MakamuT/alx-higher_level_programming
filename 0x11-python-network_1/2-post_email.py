#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body
"""
import sys
import urllib.request
import urllib.parse


if __name__ = '__main__':
    DATA = DATA.encode('ascii')
    DATA = urllib.parse.urlencode({"email": email})
    url = argv[1]
    argv = sys.argv
    email = argv[2]

    with urllib.request.urlopen(url, DATA) as response:
        print(response.read().decode('utf-8'))
