import random
'''
1 for snake
-1 for  water
0 for gun
'''

# computer = -1
computer=random.choice([-1,0,1])
yourstr=input("Enter the Choice : ")
yourDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=yourDict[yourstr]

print(f"Your Choice {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer==you):
    print("It's a Draw")

else:
 if(computer==-1 and you==1):
    print("You Win!")

 elif(computer==-1 and you==0):
    print("You Lose!")

 elif(computer==1 and you==-1):
    print("You Lose!")

 elif(computer==1 and you==0):
    print("You Win!")

 elif(computer==0 and you==-1):
    print("You Win!")

 elif(computer==0 and you==1):
    print("You Lose!")

 else:
   print("Something went wrong")

