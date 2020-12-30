Calculations=["Addition:1", "Subtraction:2", "Division:3", "Multiplication:4", "Average:5"]
for x in Calculations:
    print(x)

option=int(input("Choose an option "))
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if option==1:
    output= num1+num2
    print(output)
elif option==2:
    output= num1-num2
    print(output)
elif option==3:
    output= num1/num2
    print(output)
elif option==4:
    output= num1*num2
    print(output)
elif option==5:
    num3=int(input("Enter third number: "))
    num4=int(input("Enter fourth number: "))
    results=[num1,num2,num3,num4]
    output=sum(results)/len(results)
    print(output)
if output<0:
    print("NEGATIVE")
