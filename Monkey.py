def cal(x, a, b):
    day = 0
    height = 0
    while height < x:
        day += 1
        height += a  
        if height >= x:
            break     
        height -= b 
    print("Days needed:", day)

# Calls
cal(30, 10, 5)   
cal(25, 7, 4) 