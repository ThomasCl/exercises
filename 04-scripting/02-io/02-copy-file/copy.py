import sys


with open(sys.argv[1], 'r') as input:
    print(file.read())
    sys.argv[2].write(input.read)