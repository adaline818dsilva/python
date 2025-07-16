heads = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))
flag=False
for hens in range(heads):
    cows=heads-hens
    if(cows*4 + hens*2 == legs):
         
        print("Number of hens:", hens)
        print("Number of cows:", cows)
        flag=True
if(not flag):
    print("NO SOLUTION")
