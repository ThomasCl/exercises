import re
def contains_no_a(string):
    re.fullmatch('[^a]*',string)