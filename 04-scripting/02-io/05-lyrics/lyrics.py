import json
import sys
import urllib.request


artist = sys.argv[1].replace(' ', '%20')
title = sys.argv[2].replace(' ', '%20')


with urllib.request.urlopen('https://api.lyrics.ovh/v1/' + artist +  '/' + title) as file:
    data = json.loads(file.read())
    print(data['lyrics'])