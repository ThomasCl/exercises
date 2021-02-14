# Write your code here
def count_turns(ns):
    stijgend = True
    m = 0
    for i,j in zip(ns,ns[1:]):
        if i == j:
            stijgend = stijgend
        elif i<j:
            if stijgend == False:
                m += 1
            stijgend = True
        elif i>j:
            if stijgend == True:
                m += 1
            stijgend = False
    return m