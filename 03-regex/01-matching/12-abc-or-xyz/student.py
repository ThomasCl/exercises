import re

def abc_or_xyz(string):
    re.fullmatch('(abc)| (xyz)',string)