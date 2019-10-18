import socket

s = socket.socket()
print("Socket olusturma basarili")

port = 13579

s.bind(('',port))
print("socket %s portu ile iliskilendirildi" %(port))

s.listen(5)
print("socket porttan dinleme yapiyor")

while True:
    c,addr = s.accept()
    print(addr,"bağlandı")

    c.send('Baglanti için tesekkurler')

    c.close()

