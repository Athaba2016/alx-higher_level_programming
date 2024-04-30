#!/usr/bin/python3
"""
sends requst to URL and response body is displayed
"""
if _name__ == "__main__":
    url = sys.
    urllib import request, error
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as resp:
        except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
