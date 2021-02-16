# Write your code here
def countdown(n):
    if n == 1:
        return "1"
    return str(n) + ", " + countdown(n-1)