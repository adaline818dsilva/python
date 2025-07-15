n=int(input("enter the number"))
c=0
if n <= 1:
    print("Not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            c += 1

    if c == 0:
        print("prime")
    else:
        print("not prime")


