
calculator_on = True
current_result = 0.0
num_calc = 0
sum_calc = 0.0
avg_calc = 0.0
print('Current Result: 0.0')
print('\nCalculator Menu')
print('-' * 15)
print('0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average')

while calculator_on:
    user_choice = input('\nEnter Menu Selection: ')



    if user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5' or user_choice == '6':
        num_calc = num_calc + 1
        first_operand = (input('Enter first operand: '))
        second_operand = (input('Enter second operand: '))
        if first_operand == 'RESULT':
            first_operand = current_result
        if second_operand == 'RESULT':
            second_operand = current_result


        if user_choice == '1':
            first_operand = float(first_operand)
            second_operand = float(second_operand)
            current_result = first_operand + second_operand
            sum_calc = sum_calc + current_result
            print(f'\nCurrent Result: {current_result}')
            print('\nCalculator Menu')
            print('-' * 15)
            print('0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average')


        elif user_choice == '2':
            first_operand = float(first_operand)
            second_operand = float(second_operand)
            current_result = first_operand - second_operand
            sum_calc = sum_calc + current_result
            print(f'\nCurrent Result: {current_result}')
            print('\nCalculator Menu')
            print('-' * 15)
            print('0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average')


        elif user_choice == '3':
            first_operand = float(first_operand)
            second_operand = float(second_operand)
            current_result = first_operand * second_operand
            sum_calc = sum_calc + current_result
            print(f'\nCurrent Result: {current_result}')
            print('\nCalculator Menu')
            print('-' * 15)
            print('0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average')


        elif user_choice == '4':
            first_operand = float(first_operand)
            second_operand = float(second_operand)
            current_result = first_operand / second_operand
            sum_calc = sum_calc + current_result
            print(f'\nCurrent Result: {current_result}')
            print('\nCalculator Menu')
            print('-' * 15)
            print('0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average')


        elif user_choice == '5':
            first_operand = float(first_operand)
            second_operand = float(second_operand)
            current_result = first_operand ** second_operand
            sum_calc = sum_calc + current_result
            print(f'\nCurrent Result: {current_result}')
            print('\nCalculator Menu')
            print('-' * 15)
            print('0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average')


        elif user_choice == '6':
            first_operand = float(first_operand)
            second_operand = float(second_operand)
            import math
            current_result = math.log(second_operand, first_operand)
            sum_calc = sum_calc + current_result
            print(f'\nCurrent Result: {current_result}')
            print('\nCalculator Menu')
            print('-' * 15)
            print('0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average')


    elif user_choice == '7' and num_calc == 0:
        print('\nError: No calculations yet to average!')


    elif user_choice == '7':
        first_operand = float(first_operand)
        second_operand = float(second_operand)
        print(f'Sum of calculations: {sum_calc}')
        print(f'Number of calculations: {num_calc}')
        avg_calc = round(sum_calc / num_calc, 2)
        print(f'Average of calculations: {avg_calc}')


    elif user_choice == '0':
        calculator_on = False
        print('\nThanks for using this calculator. Goodbye!')



    else:
        print('\nError: Invalid selection!')