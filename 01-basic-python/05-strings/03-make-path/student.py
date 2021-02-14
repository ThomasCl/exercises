# Write your code here
def make_path(parts):
    m = ""
    for i in parts:
        m +=(i + "/")
    return(m[:-1])