s=input("enter your password")
dg=0
lw=0
up=0
sp=0
if(len(s)>7):
   for i in s:
      if(i.isupper()):
        up=up+1
      elif(i.islower()):
        lw=lw+1
      elif(i.isdigit()):
        dg=dg+1
      else:
        sp=sp+1

   if(dg>0 and sp>0 and lw>0 and up>0):
        print("GOOD PASSWORD")
   else:
        print("BAD PASSWORD")
else:
  print("BAD PASSWORD DUE TO LESS CHARACTERS")
 





