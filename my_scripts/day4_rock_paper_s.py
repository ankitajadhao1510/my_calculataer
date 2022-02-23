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

option = [rock, paper, scissors]
user = int(input('type 0 for rock, 1 for paper, 2 for scissors '))
print(option[user])

computer = random.randint(0, 1)
print('computer_choice:')
print(option[computer])

if user >= 3 or user < 0:
    print('invalid option')
elif user == computer:
    print('drow')
elif user < computer:
    print('you loss')
elif user > computer:
    print('you win')
elif user==0 and computer== 2:
    print('you win')
elif user==2 and computer==0:
    print('you loss')