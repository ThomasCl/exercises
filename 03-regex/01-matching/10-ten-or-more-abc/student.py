import re

def ten_or_more_abc(string):
    re.fullmatch('(abc){10,}', string)