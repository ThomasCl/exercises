# Write your code here
def contains_duplicates(xs):
    xs = sorted(xs)
    for i in range(len(xs)-1):
        if xs[i] == xs[i+1]:
            return True
    return False