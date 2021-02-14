# Write your code here
def word_count(string):
    m = 1
    for i in string:
        if i == " ":
            m += 1
    return m
