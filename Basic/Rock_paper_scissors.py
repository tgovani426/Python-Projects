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
import random
game=[rock,paper,scissors]
x=int(input("What to choose? Type 0 for Rock, 1 for paper and 2 for Scissors.\n"))

if x==0:
    a=rock
    b=random.choice(game)
    print("you chose",rock)
    print("computer chose:",b)
    if b==rock:
        print("draw")
    elif b==scissors:
        print("You lose!")
    elif b== paper:
        print("You win!")


if x==1:
    b=random.choice(game)
    print("you chose",paper)
    print("computer chose:",b)
    if b==rock:
        print("you win")
    elif b==scissors:
        print("You lose!")
    elif b== paper:
        print("Draw!!")

if x==2:
    a=rock
    b=random.choice(game)
    print("you chose",scissors)
    print("computer chose:",b)
    if b==rock:
        print("You lose")
    elif b==scissors:
        print("draw!!")
    elif b== paper:
        print("You win!")
        





