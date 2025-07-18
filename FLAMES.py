boy=input("enter the boy's name:")
girl=input("enter the girl's name:")
a1=list(boy)
a2=list(girl)
for i in range(len(boy)):
    for j in range(len(girl)):
        if(a1[i]==a2[j]):
            a1[i]='2'
            a2[j]='2'
for i in a1:
    if(i=='2'):
        a1.remove(i)
for i in a2:
    if(i=='2'):
        a2.remove(i)
num=len(a1)+len(a2)
print(num)
ans=['F','L','A','M','E','S']
index=0
while(len(ans)!=1):
   index=(index+(num-1))%len(ans)
   ans.pop(index)
print("the relation is", ans[0]) 
     

