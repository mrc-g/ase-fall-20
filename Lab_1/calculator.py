import math

def sum(m, n):
    sign = 1 if n > 0 else -1
    n = abs(n)
    while n != 0:
        m += sign
        n -= sign
    return m

def divide(m, n):
    i = 0
    sign = 1 if sign(m) == sign(n) else -1

    while m >= n:
        m -= n
        i += 1

    return i*sign