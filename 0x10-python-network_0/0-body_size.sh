#!/bin/bash
# write script to get the body size of a reguest
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
