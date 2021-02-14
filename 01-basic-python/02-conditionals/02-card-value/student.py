# Write your code here
def card_value(string):
    list = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
    for i in range(len(list)):
        if(list[i] == string):
            return(i+1)