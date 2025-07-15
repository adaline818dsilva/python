a=int(input("enter string"))
sum=0
while(a>0):
    sum=sum+a%10
    a=a//10
print("sum of digits ",sum)