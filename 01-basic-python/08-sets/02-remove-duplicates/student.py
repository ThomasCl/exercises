# Write your code here
def remove_duplicates(xs):
    set s = []
    for i in range[xs]:
        if xs[i] not in s:
            s.add(xs[i])
        xs = xs[:i] + xs[i+1:]
    return xs