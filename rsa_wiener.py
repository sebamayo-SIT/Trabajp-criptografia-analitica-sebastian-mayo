# rsa_wiener.py (demo)
from math import isqrt
import math
def continued_fraction(n, d):
    cf = []
    while d:
        q = n // d
        cf.append(q)
        n, d = d, n - q * d
    return cf
def convergents(cf):
    convs = []
    for i in range(len(cf)):
        num, den = 1, 0
        for a in reversed(cf[:i+1]):
            num, den = a * num + den, num
        convs.append((num, den))
    return convs
def is_perfect_square(n):
    r = int(math.isqrt(n))
    return r*r == n
def wiener_attack(e, n):
    cf = continued_fraction(e, n)
    convs = convergents(cf)
    for (k, d) in convs:
        if k == 0: continue
        if (e * d - 1) % k != 0: continue
        phi = (e * d - 1) // k
        s = n - phi + 1
        discr = s*s - 4*n
        if discr >= 0 and is_perfect_square(discr):
            t = int(math.isqrt(discr))
            if (s + t) % 2 == 0:
                p = (s + t)//2
                q = (s - t)//2
                if p*q == n:
                    return d, p, q
    return None
def demo():
    p = 1000003; q = 1000033; n = p*q
    d = 123457; phi = (p-1)*(q-1); e = pow(d, -1, phi)
    print("n=", n, "e=", e, "d(real)=", d)
    res = wiener_attack(e, n)
    print("resultado:", res)
if __name__ == '__main__': demo()