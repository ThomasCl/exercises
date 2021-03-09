# Write your code here
def remove_duplicates(xs):
    s = set()
    r = []
    for i in xs:
        if i not in s:
            s.add(i)
            r.append(i)
    return r