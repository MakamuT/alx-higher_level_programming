#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    import urllib.request
    import sys
    import urllib.error

    if len(sys.argv) != 2:
        print("Usage: ./script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print(f"HTTP Error: {err.code} {err.reason}")
    except urllib.error.URLError as err:
        print(f"URL Error: {err.reason}")
