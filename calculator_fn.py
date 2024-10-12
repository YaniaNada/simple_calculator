def calculate(a,b, operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        if b!= 0:
            return a/b
        else:
            return 'Error: division by zero'
    elif operator == ('Q' or 'q'):
        return 'Operation cancelled'
    else:
        print("Invalid input.")