import fn_calculator
import fn_get_inputs
import fn_quit_or_continue

while True:
    print('For the first number')
    a = fn_get_inputs.get_input()

    print('For the second number')
    b = fn_get_inputs.get_input()

    print('Select the operator:  + for addition, - for subtraction, * for multiplication, and / for division. To quit select Q.')
    operator = input('Please enter the operator:')

    print('result:')
    print(fn_calculator.calculate(a,b, operator))
    x= input('Enter Q to exit or C to continue with new operation: ')
    result = fn_quit_or_continue.q_or_c(x)
    if result == 'operation cancelled.':
        print(result)
        break
    elif result == 'New operation:':
        print(result)
        continue

