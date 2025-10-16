# sim_encrypt.py
import os
P1 = b"Hola profesor, esto es un mensaje secreto 1."
P2 = b"Estimado profesor, este mensaje secreto 2 es similar."
keystream = os.urandom(max(len(P1), len(P2)))
C1 = bytes(a^b for a,b in zip(P1, keystream))
C2 = bytes(a^b for a,b in zip(P2, keystream))
print("C1 hex:", C1.hex())
print("C2 hex:", C2.hex())