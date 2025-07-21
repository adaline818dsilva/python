def prime_factors(n):
    if n==1:
        return
    i = 2
    while (n%i!=0):
        i=i+1
    print(i, end=" ")
    prime_factors(n//i)

n= int(input("Enter a number: "))
prime_factors(n)