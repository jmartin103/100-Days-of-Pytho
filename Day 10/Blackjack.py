import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2: # Has a blackjack, return 0
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'It\'s a draw!'
    elif computer_score == 0:
        return 'Computer got a blackjack! You lose!'
    elif user_score == 0:
        return 'You got a blackjack! You win!' 
    elif user_score > 21:
        return 'You went over! You lose!'
    elif computer_score > 21:
        return 'Computer went over! You win!'
    elif user_score > computer_score:
        return 'You win!'
    else:
        return 'You lose!'

def main():
    user_cards = []
    computer_cards = []

    # Deal user and computer two randomly generated cards each
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
            
    game_over = False

    while game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, your current score: {user_score}')
        print(f'Computer\'s first card: {computer_cards[0]}')    
        
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input('Would you like to deal another card? Type \'y\' to deal or \'n\' to pass: ').lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f'Computer\'s first card: {computer_cards[0]}')
                print(f'Your cards: {user_cards}, your current score: {user_score}')
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f'Your final hand: {user_cards}, your final score: {user_score}')
    print(f'Computer\'s final hand: {computer_cards}, computer\'s final score: {computer_score}')
    result = compare(user_score, computer_score)
    print(result)

    play_again = input('Would you like to play again? Type \'y\' or \'n\': ').lower()
    if play_again == 'y':
        main()
    elif play_again == 'n':
        game_over = True
    
main()