# cbc_bitflip_demo.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
BLOCK = AES.block_size
key = get_random_bytes(16)
iv = get_random_bytes(BLOCK)
plaintext = b"user=guest;uid=1000;role=guest;"
cipher = AES.new(key, AES.MODE_CBC, iv)
ct_body = cipher.encrypt(pad(plaintext, BLOCK))
ct = iv + ct_body
print("Ciphertext (hex):", ct.hex())