n=int(input("Enter num of teams:"))
teams=[]
for i in range(n):
    a=input("Enter name of team:")
    teams.append(a)
meet=int(input("Enter num of meeting bw one pair:"))

match=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            match.append((teams[i],teams[j]))


print("---------")
index=1
for i in match:
    print("Match {}: {} vs {}".format(index,i[0],i[1]))
