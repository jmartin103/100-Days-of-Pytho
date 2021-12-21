from GameData import data
import random

def generate_random_data():
    return random.choice(data)

def format_data(acct_data):
    name = acct_data["name"]
    description = acct_data["description"]
    country = acct_data["country"]

    return (f'{name}, a {description} from {country}')

def check_answer(guess, followers_of_a, followers_of_b):
    if followers_of_a > followers_of_b:
        return guess == 'a'
    else:
        return guess == 'b'

def main():
    is_correct = True
    score = 0

    account_a = generate_random_data()
    account_b = generate_random_data()
    
    while is_correct:
        account_a = account_b
        account_b = generate_random_data()

        print(f'A: {format_data(account_a)}')
        print(f'B: {format_data(account_b)}')

        guess = input('Who has more followers? Type \'a\' or \'b\': ').lower()
        
        followers_of_a = account_a['follower_count']
        followers_of_b = account_b['follower_count']

        is_correct_guess = check_answer(guess, followers_of_a, followers_of_b)

        if is_correct_guess:
            is_correct = True
            score += 1
            print(f'You\'re correct! Current score: {score}')
        else:
            is_correct = False
            print(f'Sorry, that\'s wrong. Final score: {score}')

main()