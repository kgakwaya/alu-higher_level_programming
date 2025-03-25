#!/usr/bin/python3
"""Fetches a URL status using urllib package."""

import urllib.request

if __name__ == "__main__":
    try:
        url = "https://intranet.hbtn.io/status"
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except urllib.error.URLError:
        # Fallback to local test URL if main URL fails
        url = "http://0.0.0.0:5050/status"
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8'))) 
