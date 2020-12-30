x=str(input("Enter a string value "))
Alphabets=Numbers=0
for i in range(len(x)):
    if ((x[i]>="a" and x[i]<="z") or x[i]>="A" and x[i]<="Z"):
        Alphabets=Alphabets+1
    elif ((x[i]>="0" and x[i]<="9")):
        Numbers=Numbers+1
print("Letters ", Alphabets)
print("Digits ", Numbers)

