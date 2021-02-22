def greatest_sum(ns):
    winner = 0
    ret = (0,0)
    for i in range(ns):
        for j in range(i, ns):
            tot = 0
            for k in range (i, j):
                tot += ns[k]
            if tot > winner:
                winner = tot
                ret = (i,j)
    return ret
