import time
names=[]
marks=[]
for i in range(3):
    n=input("enter the name:")
    names.append(n)
    student=[]
    for j in range(3):
        m=int(input("enter the marks of the student:".format(j+1)))
        student.append(m)
    marks.append(student)
per=[]
for i in marks:
    res=sum(i)//3
    per.append(res)
time.sleep(3)
print("--------------------")
for i in range(3):
    print("{}.{} : {}".format(i+1,names[i],per[i]))