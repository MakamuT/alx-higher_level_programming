#!/usr/bin/bash
""" fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    import urllib.request
    import sys

    argv = sys.argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))
