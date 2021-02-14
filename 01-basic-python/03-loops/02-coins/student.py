# Write your code here
def coins(one, two, five, goal):
    for i in range(five+1):
        for j in range(0,two+1):
            for k in range(0,one+1):
                if (i*5)+(j*2)+(k*1) == goal:
                    return True
    return False