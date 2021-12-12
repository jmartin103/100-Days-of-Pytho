import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_guess(guess, random_num, turns):
    if guess > random_num:
        print('Too high. Try again.')
        return turns - 1
    elif guess < random_num:
        print('Too low. Try again.')
        return turns - 1
    else:
        print(f'You got it! The number was {random_num}.')

def generate_random_number():
    return random.randint(1, 100)

def set_difficulty():
    level = input('Choose a difficulty. Type \'easy\' or \'hard\'. ').lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS

def main():
    print('I\'m thinking of a number between 1 and 100. Can you guess it?')
    random_num = generate_random_number()
    attempts = set_difficulty()

    guess = 0
    while guess != random_num:
        print(f'You have {attempts} attempts to guess the number.')
        guess = int(input('Enter your guess: '))
        attempts = check_guess(guess=guess, random_num=random_num, turns=attempts)

        if attempts == 0:
            print(f'You lose! The number I was thinking of was {random_num}.')
            break
        elif guess != random_num:
            print('Please make another guess.')

main()