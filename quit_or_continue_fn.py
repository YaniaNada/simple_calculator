def q_or_c(x):
    x = x.upper()
    if x == 'Q':
        return 'operation cancelled.'
    elif x == 'C':
        return 'New operation:'