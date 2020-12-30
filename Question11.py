#Let's suppose the lucky number is 220

counter=0
while counter<5:
    counter+=1
    number=int(input("Guess a lucky number "))
    
    if number==220:
        print("Good Guess!")
        break  
            
    elif number!=220 and counter<5:
        print("Try Again")

if counter==5:
    print("Sorry, but that was not very successful")