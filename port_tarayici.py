import socket
from concurrent.futures import ThreadPoolExecutor


hedef="127.0.0.1"


def tara(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sonuc=s.connect_ex((hedef,port))
    s.close()
    if sonuc==0:
        return port
    return None

with ThreadPoolExecutor(max_workers=100) as f:
    sonuclar=f.map(tara,range(1,1025))

for i in sonuclar:
    if i is not None:
        print(f"{i} açık")
print("Tarama Bitti")