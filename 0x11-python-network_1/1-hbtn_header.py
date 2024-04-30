#!/usr/bin/python3

""" script that takes URL,
sends URL a request
displays X-Requst-Id value
variable found in the response header.
"""

import sys
import urllib.request

if _name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(resp.headers).get("X-Request-Id"))
