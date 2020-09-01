import numpy as np

c = 3E8
def BalmerLines(n):
    '''
    -------------------------------------------
    BalmerLines(n)
    -------------------------------------------
    Returns the value of the wavelenght lambda
    (in meters) for a given value of n in the
    Balmer series (n <= 3).

    If n < 3 returns None
    -------------------------------------------
    '''
    if n >= 3:
        return n/c
    else:
        return "None"

def BalmerLines2(arg):
    return 0
