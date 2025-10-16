# find_by_time.py
import hashlib, datetime
objetivo = "REEMPLAZAR_CON_HASH_OBJETIVO"
inicio = datetime.datetime(2025,10,14,10,0,0)
fin = datetime.datetime(2025,10,14,10,5,0)
for ts in range(int(inicio.timestamp()), int(fin.timestamp())+1):
    if hashlib.md5(str(ts).encode()).hexdigest() == objetivo:
        print("Encontrado:", ts, datetime.datetime.fromtimestamp(ts))
        break
else:
    print("No encontrado en el rango")