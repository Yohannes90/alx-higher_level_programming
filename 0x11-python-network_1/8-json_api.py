#!/usr/bin/python3
""" takes in a letter and sends POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if (response == {}):
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
