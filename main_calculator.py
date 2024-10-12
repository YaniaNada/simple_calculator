import calculator_fn
import get_inputs_fn
import quit_or_continue_fn

while True:
    print('For the first number')
    a = get_inputs_fn.get_input()

    print('For the second number')
    b = get_inputs_fn.get_input()

    print('Select the operator:  + for addition, - for subtraction, * for multiplication, and / for division. To quit select Q.')
    operator = input('Please enter the operator:')

    print('result:')
    print(calculator_fn.calculate(a,b, operator))
    x= input('Enter Q to exit or C to continue with new operation: ')
    result = quit_or_continue_fn.q_or_c(x)
    if result == 'operation cancelled.':
        print(result)
        break
    elif result == 'New operation:':
        print(result)
        continue

