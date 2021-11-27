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

#Write your code below this line 👇
choice = int(input('Choose 0 for rock, 1 for paper, or 2 for scissors: '))
rps = [rock, paper, scissors]
random_integer = random.randint(0, 2)
player_choice = rps[choice]
computer_choice = rps[random_integer]

print(f'You chose {player_choice}')
print(f'Computer chose {computer_choice}')

if choice == random_integer:
  print('It\'s a draw!')
elif choice == 0 and random_integer == 1:
  print('You lose!')
elif choice == 0 and random_integer == 2:
  print('You win!')
elif choice == 1 and random_integer == 2:
  print('You lose!')
elif choice == 1 and random_integer == 0:
  print('You win!')
elif choice == 2 and random_integer == 0:
  print('You lose!')
elif choice == 2 and random_integer == 1:
  print('You win!')
elif choice > 2 or choice < 0:
  print('Invalid choice; you lose!')