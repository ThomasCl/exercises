import sys

with open(sys.argv[1], 'r') as inp:
    with open(sys.argv[2], 'w') as out:
        out.write(inp.read())