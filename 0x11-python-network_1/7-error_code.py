#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body
    of the response (decoded in utf-8)
"""

import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
