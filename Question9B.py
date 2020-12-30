#PART B: Let's suppose the lucky number is 220

while True:
    number=int(input("Guess a lucky number "))
    if number==220:
        break
    if number!=220:
        print("Do you want to guess again?")
        answer=str(input("Yes/No? "))
        if answer=="No":
            break
        if answer=="Yes":
            continue
            