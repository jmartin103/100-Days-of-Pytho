#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''

# Generate a random password from user inputs given
for letter in range(1, nr_letters + 1):
  random_letter = random.randint(0, len(letters) - 1)
  letter = letters[random_letter]
  password += letter

for symbol in range(1, nr_symbols + 1):
  random_sym = random.randint(0, len(symbols) - 1)
  symbol = symbols[random_sym]
  password += symbol

for number in range(1, nr_numbers + 1):
  random_num = random.randint(0, len(numbers) - 1)
  number = numbers[random_num]
  password += number

password_as_list = list(password) # Convert to list for shuffling

random.shuffle(password_as_list)
randomized_password = ''.join(str(char) for char in password_as_list)
print(f'Your new password is {randomized_password}')