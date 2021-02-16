# Write your code here
def format_grades(grades):
    st=""
    for i in grades:
        st += i + ": " + str(rounded(grades[i])) + "\n"
    return st


def rounded(li):
    s = sum(li)
    return round(s/len(li))