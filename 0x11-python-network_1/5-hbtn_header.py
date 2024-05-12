#!/usr/bin/python3
"""sends a request to the URL"""
import sys
import requests
sys.modules['requests'] = requests


if __name__ == '__main__':
    url = sys.argv[1]

    try:
        response = requests.get(url)

        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(f"X-Request-Id value: {request_id}")
        else:
            print("X-Request-Id header not found in the response")


    except requests.RequestException as e:
        print(f"Error: {e}")
