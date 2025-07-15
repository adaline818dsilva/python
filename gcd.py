a=int(input("enter the number"))
b=int(input("enter the number"))
rem=0
while(b!=0):
    rem=a%b
    a=b
    b=rem
print(f"gcd of {a} and {b} is {a}")

