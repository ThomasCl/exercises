# Write your code here
def sum_squares(ns):
    res = 0
    ns = [n *n for n in ns]
    for i in ns:
        res += i
    return res