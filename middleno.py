a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
if a>=b and a<=c:
    print("the middle number is ",a)
elif b>=a and b<=c:
    print("the middle number is ", b)
else:
    print("the middle no is ",c)