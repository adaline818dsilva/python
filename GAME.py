import random
name1=input("Enter Player 1:")
name2=input("Enter Player 2:")
print("Comp has fixed 5 nums in range of 1 to 10")
print("You gys have to guess it...Ready?")

nums=[]
while(len(nums)!=5):
    d=random.randint(1,10)
    if(d not in nums):
        nums.append(d)
print("-------------")
s1=0
s2=0
player1=[]
player2=[]
for i in range(3):
    print("---------round{}---------".format(i+1))
    print("Dear {} guess your choice".format(name1))
    ch=int(input())
    while(ch in player1 or ch in player2):
        ch=int(input("It is alraedy taken choose another one"))
    player1.append(ch)
    if(ch in nums):
        print("--->> CORRECT")
        s1=s1+1
    else:
        print("------>>WRONG")
     
    print("Dear {} guess your choice".format(name2))
    ch=int(input())
    while(ch in player1 or ch in player2):
        ch=int(input("It is alraedy taken choose another one"))
    player2.append(ch)
    if(ch in nums):
        print("--->> CORRECT")
        s2=s2+1
    else:
        print("------>>WRONG")
print("----------")
print("Lets have summary")
print("Comp has fixed",nums)
print("{} has chosen {}".format(name1,player1))
print("{} score is {}".format(name1,s1))
print("{} has chosen {}".format(name2,player2))
print("{} score is {}".format(name2,s2))


print("-----------")
if(s1>s2):
    print("{} is the winner".format(name1))
elif(s2>s1):
    print("{} is the winner".format(name2))
else:
    print("Drawn")

