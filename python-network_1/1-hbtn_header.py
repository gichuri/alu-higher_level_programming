
#!/usr/bin/python3


"""display the x-Request-ID variale"""

import sys
import urllib

def fetcher():
    """fetcher"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header["X-Request-Id"])

if __name__ == "__main__":
    fetcher()
