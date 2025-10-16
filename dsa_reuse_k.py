# dsa_reuse_k.py (demo)
from Crypto.Util.number import inverse
import hashlib
def H(m): return int.from_bytes(hashlib.sha1(m).digest(),'big')
q = 1753; p = q*127 + 1; g = pow(2, (p-1)//q, p); x = 1234
k = 4567
def sign(msg):
    hm = H(msg) % q
    r = pow(g, k, p) % q
    s = (inverse(k, q) * (hm + x * r)) % q
    return r, s, hm
m1 = b"Mensaje uno"; m2 = b"Mensaje dos"
r1,s1,h1 = sign(m1); r2,s2,h2 = sign(m2)
print(r1,s1,h1); print(r2,s2,h2)
k_rec = ((h1 - h2) * inverse(s1 - s2, q)) % q
x_rec = ((s1 * k_rec - h1) * inverse(r1, q)) % q
print('k_rec', k_rec, 'x_rec', x_rec, 'orig x', x)