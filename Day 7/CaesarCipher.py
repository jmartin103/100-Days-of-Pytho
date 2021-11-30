import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    cipher_text = ''

    for char in range(len(text)):
        if text[char] not in alphabet:
            cipher_text += text[char]
            continue
        else:
            char = alphabet.index(text[char % 26])
            char_shift = (char + shift) % 26
            encrypted_letter = alphabet[char_shift]
            cipher_text += encrypted_letter
    
    return cipher_text

def decrypt(text, shift):
    decrypted_text = ''

    for char in range(len(text)):
        if text[char] not in alphabet:
            decrypted_text += text[char % 26]
            continue
        else:
            letter = alphabet.index(text[char])
            letter_shift = (letter - shift) % 26
            decrypted_letter = alphabet[letter_shift]
            decrypted_text += decrypted_letter
    
    return decrypted_text

def run_again():
    choice = input('Do you want to run the program again? Type \'yes\' or \'no\' ').lower()
    if choice == 'yes':
        main()
    elif choice == 'no':
        print('Goodbye!')
        sys.exit()

def main():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == 'encode':
        print(encrypt(text, shift))
    elif direction == 'decode':
        print(decrypt(text, shift))
    run_again()

main()