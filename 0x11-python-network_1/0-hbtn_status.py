#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

if _name_== "_main_":
   request = urllib.request.Request(" https://alx-intranet.hbtn.io/status.")
   with urllib.request.urlopen as request
   body = response.read()
   print("Body response:")
   print ("\t- type: {}".format(type(body)))
   print("\t- content: {}".format(body))
