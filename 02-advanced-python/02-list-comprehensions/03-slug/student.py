# Write your code here
def slug(string):
    string = string.lower()
    li = string.split()
    s = ""
    for i in range(1, len(li)):
        s += li[i] + "-"
    return s + li[0]
