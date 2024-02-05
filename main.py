import random
from art import rock, paper, scissors


option = [rock, paper, scissors]

you_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if you_choose >= 3 or you_choose < 0: 
  print("You typed an invalid number, you lose!")
else:
  
  print(option[you_choose])
  
  print("Computer choose:")
  computer_choose_index = random.randint(0, 2)
  computer_choose = option[computer_choose_index]
  print(computer_choose)
  
  
  if you_choose == 0 and computer_choose_index == 2:
    print("You win!")
  elif computer_choose_index == 0 and you_choose == 2:
    print("You lose!")
  elif computer_choose_index > you_choose:
    print("You lose!")
  elif you_choose > computer_choose_index:
    print("You win!")
  elif you_choose == computer_choose_index:
    print("It's a draw")