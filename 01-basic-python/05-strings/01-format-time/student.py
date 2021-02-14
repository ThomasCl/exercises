# Write your code here
def format_time(h, m, s):
    h = str(h)
    m = str(m)
    s = str(s)
    if len(h) == 1:
        h = "0"+h
    if len(m) == 1:
        m = "0" + m
    if len(s) == 1:
        s = "0" + s
    return h + ":" + m + ":" + s