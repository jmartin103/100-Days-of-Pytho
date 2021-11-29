import random

word_list = ['city', 'computer', 'science', 'college', 'student', 'list', 'house', 'country', 'aardvark', 'camel', 'dog', 
'laptop', 'professor', 'chemistry', 'physics', 'philosophy', 'sociology', 'math', 'pizza', 'avocado', 'mayonnaise', 'hamburger', 
'website', 'tutorial', 'idea', 'launch', 'boy', 'girl', 'nurse', 'interstate', 'road', 'needle', 'doctor', 'breathe', 'space', 
'movie', 'basketball', 'baseball', 'health', 'funeral', 'wedding', 'show', 'sneeze', 'allergy', 'freeway', 'town', 'burn', 'fine']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for i in range(word_length):
    display += "*"

attempts_remaining = 6

while attempts_remaining > 0:
    display_str = ''.join(display)
    print(str(display_str))
    if display_str == chosen_word:
        print('You Win!')
        break
    else:
        print(f'You have {attempts_remaining} attempts remaining.')
        guess = input("Guess a letter: ").lower()
        if guess not in chosen_word:
            print('Incorrect guess!')
            attempts_remaining -= 1
        else:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter

    if attempts_remaining == 0:
        print(f'Game Over! The word we were looking for is {chosen_word}')