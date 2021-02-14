# Write your code here
def includes(xs, ys):
    for i in ys:
        init = False
        for j in xs:
            if i == j:
                init = True
        if init is False:
            return False
    return True
                