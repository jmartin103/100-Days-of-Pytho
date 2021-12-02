def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('ERROR: Can\'t divide by zero!')

def main():
    operations = {
        '+': 'Add',
        '-': 'Subtract',
        '*': 'Multiply',
        '/': 'Divide'
    }
  
    num1 = int(input('What is the first number? '))
    num2 = int(input('What is the second number? '))

    for op in operations:
        operation = operations[op]
        print(f'{op}: {operation}')
  
    choice = input('Please choose an operation from above (+, -, *, or /): ')

    result = 0
    if choice == '+':
        result = add(num1, num2)
        print(f'{num1} + {num2} = {result}')
    elif choice == '-':
        result = subtract(num1, num2)
        print(f'{num1} - {num2} = {result}')
    elif choice == '*':
        result = multiply(num1, num2)
        print(f'{num1} * {num2} = {result}')
    elif choice == '/':
        result = divide(num1, num2)
        if num2 != 0:
            print(f'{num1} / {num2} = {result}')
  
main()