import sys
import re

with open(sys.argv[1], 'rw') as file:
    input = file.read()
    text = re.sub('#*','', input)