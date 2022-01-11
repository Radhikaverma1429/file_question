a=open("exercise.txt","r")
j=a.readline().split()
i=0
c=0
while i<len(j):
    if "delhi" in j[i]:
      c+=1
    i+=1
print(c)
a.close()
