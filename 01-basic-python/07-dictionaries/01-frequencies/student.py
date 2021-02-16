# Write your code here
def frequencies(xs):
    dic = {}
    for i in xs:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1
    return dic