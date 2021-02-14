# Write your code here
def cakes(eggs, butter, flour):
    a = eggs//5
    b = butter//250
    c = flour//250
    if(a < b):
        small = a
    else: 
        small = b
    if(small < c):
        return small
    else:
        return c