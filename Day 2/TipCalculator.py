print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = int(input('How much tip? '))
people = int(input('How many people are splitting the bill? '))

bill_with_tip = bill + (bill * (tip / 100))

amt_each_person_pays = (bill_with_tip / people)
print(f'Each person should pay ${round(amt_each_person_pays, 2)}')
