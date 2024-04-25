#!/bin/bash
# bash script that eas fun in breaking to http into holberton servers
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
