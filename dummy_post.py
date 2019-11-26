#!/usr/bin/env python3
################## dummy json data ##################
#
# This will send dummy json to an endpoint
#
#
# written by Jeremy Eglen
# license: Apache version 2.0
# Created: November 26, 2019
# Last Modified: November 26, 2019

import requests
import time

# dummy_data from https://next.json-generator.com/
dummy_data = {
    "_id": "5ddd435881ed7e1b4bed9b0d",
    "index": 0,
    "guid": "6758b46e-225f-4ad9-b201-9e079aaebfe7",
    "isActive": False,
    "balance": "$1,003.25",
    "picture": "http://placehold.it/32x32",
    "age": 32,
    "eyeColor": "blue",
    "name": {
      "first": "Holden",
      "last": "Austin"
    },
    "company": "NORALEX",
    "email": "holden.austin@noralex.com",
    "phone": "+1 (896) 519-2820",
    "address": "912 Verona Place, Belva, Virginia, 6884",
    "about": "<TypeError: loremIpsum is not a function>",
    "registered": "Friday, June 22, 2018 4:29 PM",
    "latitude": "41.335917",
    "longitude": "65.696153",
    "tags": [
      "<TypeError: loremIpsum is not a function>",
      "<TypeError: loremIpsum is not a function>",
      "<TypeError: loremIpsum is not a function>",
      "<TypeError: loremIpsum is not a function>",
      "<TypeError: loremIpsum is not a function>"
    ],
    "range": [
      0,
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9
    ],
    "friends": [
      {
        "id": 0,
        "name": "Cherie Dillon"
      },
      {
        "id": 1,
        "name": "Suzette Fulton"
      },
      {
        "id": 2,
        "name": "Clare Blackburn"
      }
    ],
    "greeting": "Hello, Holden! You have 7 unread messages.",
    "favoriteFruit": "strawberry"
  }

url = input("What's our post url? ") or "http://127.0.0.1:5000"

times = input("How many times should I post? ") or 1
times = int(times)

delay = input("How many seconds should I delay between times? ") or 0.1
delay = float(delay)

for n in range(times):
    print("Posting to {}".format(url))
    r = requests.post(url, json=dummy_data)
    print("Status was {}".format(r.status_code))
    print("Full Response:\n{}".format(r.text))
    
    print("******************\n")
    if n < times - 1:
        print("Sleeping {} seconds".format(delay))
        time.sleep(delay)
