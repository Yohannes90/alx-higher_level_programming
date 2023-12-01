#!/usr/bin/python3
""" takes in URL and an email, sends a POST request to the passed URL with the
    email as a parameter, displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], {"email": sys.argv[2]})
    print(r.text)
