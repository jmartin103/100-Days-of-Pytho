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
    num1 = int(input('What is the first number? '))

    operators = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    for op in operators:
        print(f'{op}')

    choice = input('Please choose an operator from above (+, -, *, or /): ')
    num2 = int(input('What is the second number? '))
    calc_function = operators[choice]
    result = calc_function(num1, num2)
    print(f'{num1} {choice} {num2} = {result}')

    calculate_again = 'y'
    while calculate_again == 'y':
        calculate_again = input('Would you like to perform another calculation? Type \'y\' or \'n\': ').lower()
        if calculate_again == 'n':
            print('Goodbye!')
            break
        else:
            for op in operators:
                print(f'{op}')

            choice = input('Please choose an operation from above (+, -, *, or /): ')
            num = int(input('What is the second number? '))
            calc_function = operators[choice]
            prev_result = result
            result = calc_function(prev_result, num)
            print(f'{prev_result} {choice} {num} = {result}')
            continue
main()