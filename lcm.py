a=int(input("enter the number"))
b=int(input("enter the number"))
if a>b:
    big=a
else:
    big=b
step=big
while(True):
    if(big%a==0 and big%b==0):
        print(f"lcm of {a} and {b} is {big}")
        break
    else:
        big=big+step