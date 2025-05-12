import random
computer=random.choice([-1,0,1])
yourstr=input("Enter the Choice : ")
yourDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=yourDict[yourstr]

print(f"Your Choice {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer==you):
    print("It's a Draw")

# By we have 2 numbers (variables): you and computer

else:
    if((computer-you)==-1 or (computer-you)==2):
        print("You Lose!")
    else:
        print("You Win!")

