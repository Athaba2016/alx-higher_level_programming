#!/usr/bin/python3
"""Sends a post request with  URL with a given emain.

 - Displays body of response.
"""
import sys
import urllib.parse
import urlllib.request

if _name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url,data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
