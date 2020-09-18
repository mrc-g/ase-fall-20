import math

def _sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def sum(m, n):
    sign = _sign(n)
    n = abs(n)
    while n != 0:
        m += sign
        n -= 1
    return m

def divide(m, n):
    if n == 0:
        raise ZeroDivisionError

    i = 0
    sign = 1 if _sign(n) == _sign(m) else -1

    n = abs(n)
    m = abs(m)

    while m >= n:
        m -= n
        i += 1

    return i*sign