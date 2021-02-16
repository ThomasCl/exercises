# Write your code here
def contains_duplicates(xs):
    if len(xs) == len(set(zip(xs))):
        return False
    return True