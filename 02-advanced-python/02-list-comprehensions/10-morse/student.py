# Write your code here
morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..' }
morse_rev = dict((m,l) for l,m in morse.items())

def to_morse(string):
    string = string.upper()
    m = ""
    for i in string:
        m += morse[i]
    return m


def from_morse(string):
    m = ""
    for i in string:
        m += morse_rev[i]
    return m

