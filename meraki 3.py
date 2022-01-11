a=open("meraki.txt","w") 
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(banks_list):
    a.write(banks_list[i])
    a.write("\n")
    i+=1
a.close() 