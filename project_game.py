'''
THIS IS THE ROCK-PAPER-SCISSOR-LIZARD-SPOCK GAME!!
ULTIMATE CHALLENGE!!

-2 - Rock
-1 - Paper
0 - Scissor
1 - Lizard
2- Spock
'''
import random
computer = random.choice([-2,-1, 0, 1,2])
print("Are you ready to win the ultimate challenge?")
userstr = input("Enter your choice: ")
userDict = {"Rock":-2, "Paper":-1, "Scissor": 0, "Lizard": 1, "Spock": 2}
reverseDict = {-2: "Rock", -1: "Paper", 0: "Scissor", 1:"Lizard", 2:"Spock"}

user = userDict[userstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[user]}\nComputer chose {reverseDict[computer]}")

if(computer == user):
    print("Its a draw")

else:
    if(computer ==-2 and user == -1): 
        print("You win!")

    elif(computer ==-2 and user == 0): 
        print("You lose!")

    elif(computer ==-2 and user == 1): 
        print("You lose!")

    elif(computer ==-2 and user == 2): 
        print("You win!")

    elif(computer ==-1 and user == 0):
        print("You win!")

    elif(computer ==-1 and user == -2):
        print("You lose!")

    elif(computer ==-1 and user == 1):
        print("You win!")

    elif(computer ==-1 and user == 2):
        print("You lose!")

    elif(computer ==0 and user == -1):
        print("You lose!")

    elif(computer == 0 and user == -2):
        print("You win!")

    elif(computer == 0 and user == 1):
        print("You lose!")

    elif(computer == 0 and user == 2):
        print("You win!")

    elif(computer == 1 and user == -1):
        print("You lose!")

    elif(computer == 1 and user == -2):
        print("You win!")

    elif(computer == 1 and user == 2):
        print("You lose!")

    elif(computer ==1 and user == 0):
        print("You win!")

    elif(computer == 2 and user == -1):
        print("You win!")

    elif(computer == 2 and user == -2):
        print("You lose!")

    elif(computer == 2 and user == 1):
        print("You win!")

    elif(computer == 2 and user == 0):
        print("You lose!")

     
    else:
        print("Something went wrong!")