def get_input():
    while True:
        x = input('Enter a number: ')
        if x.isnumeric():
            return float(x)
        else:
            print('Invalid input. Please try again.')

            

