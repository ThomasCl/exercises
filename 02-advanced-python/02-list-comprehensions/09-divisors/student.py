# Write your code here
def divisors(n):
    return [t for t in range(1, n+1) if n%t == 0]