# Write your code here
def is_prime(n):
    return n>1 and all(n%t!=0 for t in range(2,n))