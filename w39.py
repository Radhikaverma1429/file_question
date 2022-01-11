a=open("meraki.txt","r")
j=a.readlines()
i=0
c=0
while i<len(j):
    c+=1
    i+=1
print(c)
a.close()
