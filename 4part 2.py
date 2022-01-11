a=open("meraki 4.txt","r")
f1=open("delhi.txt","w")
f2=open("shimla.txt","w")
f3=open("other.txt","w")
d=a.read()
e=d.split("\n")
i=0
while i<len(e):
    if "delhi" in e[i]:
        f1.write(e[i])
        f1.write("\n")
    elif  "shimla" in e[i]:
        f2.write(e[i])
        f2.write("\n")
    else:
        f3.write(e[i])
        f3.write("\n")
    i+=1
a.close() 