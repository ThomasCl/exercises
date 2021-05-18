import sys
import urllib.request


with urllib.request.urlopen(sys.argv[1]) as file:
    print(file.read())