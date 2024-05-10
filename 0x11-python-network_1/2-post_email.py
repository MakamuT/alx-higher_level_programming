#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body
"""


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    DATA = urllib.parse.urlencode({"email": email})
    DATA = DATA.encode('ascii')
    url = argv[1]
    argv = sys.argv
    email = argv[2]

    with urllib.request.urlopen(url, DATA) as response:
        print(response.read().decode('utf-8'))
