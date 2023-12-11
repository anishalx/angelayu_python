import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user= int(input("What do you choose ? \nType 0 for Rock,1 for Papper or 2 for Scissors :\n"))
choose = [rock,paper,scissors]
if user >= 3 or user <0 :
    print("please enter a valid input ")
else :
    print("you choosed")
    print(f"{choose[user]}")

computer = random.randint(0,2)
print("computer chosen")
print(f"{choose[computer]}")


if  computer == 2 and user == 0:
    print("you won!")
elif computer == 0 and user == 2:
    print("you lose !")
elif computer > user :
    print("you lose!")
elif user > computer:
    print("you win!")
elif computer == user:    
    print("It's a tie!")
else :
    print("Opps! just restart the game .")





