#!/usr/bin/python3
"""module to fetch a url"""

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
	html = response.read()