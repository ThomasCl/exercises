import urllib.request
import sys
import json




with urllib.request.urlopen('http://xkcd.com/' + sys.argv[1] + '/info.0.json') as xk:
    dat = json.loads(xk.read)
    print(dat['info'])