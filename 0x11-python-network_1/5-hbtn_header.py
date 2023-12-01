#!/usr/bin/python3
""" send request to URL it took, display X-Request-Id value in header response
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
