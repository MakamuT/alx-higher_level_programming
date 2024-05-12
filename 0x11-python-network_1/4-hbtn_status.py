#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
requests = __import__('requests')


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("Body response:")
            print("\t- type: {}".format(type(response.text)))
            print("\t- content: {}".format(response.text))
        else:
            print("Error: HTTP status code {}".format(response.status_code))

    except reuests.exceptions.RequestException as e:
        print(f"Error: {e}")
