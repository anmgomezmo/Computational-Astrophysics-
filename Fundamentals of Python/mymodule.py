def BalmerLines(n):
    '''
    ------------------------------------------
    BalmerLines(n)
    ------------------------------------------
    Returns the value of the wavelenght lambda
    (in meters) for a given value of n in the
    Balmer series (n<=3).
    If n<3 returns None
    ------------------------------------------
    '''
    if n < 3:
        return None
    else:
        R = 1.09677583E7 # in untis of m^-1
        lambda_inv = R * (1/4 - 1/n**2)
        return 1/lambda_inv
