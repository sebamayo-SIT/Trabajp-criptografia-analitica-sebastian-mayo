# crib_drag.py
import binascii
def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))
C1_hex = input("Pegar C1 hex: ").strip()
C2_hex = input("Pegar C2 hex: ").strip()
C1 = binascii.unhexlify(C1_hex)
C2 = binascii.unhexlify(C2_hex)
L = min(len(C1), len(C2))
X = xor_bytes(C1[:L], C2[:L])
crib = input("Ingrese crib: ").encode()
for i in range(0, len(X)-len(crib)+1):
    frag = bytes(a ^ b for a, b in zip(crib, X[i:i+len(crib)]))
    printable = ''.join(chr(c) if 32 <= c < 127 else '?' for c in frag)
    print(f"pos {i}: {printable}")