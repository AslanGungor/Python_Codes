import socket
import sys

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Socket basarili bir sekilde olusturuldu')
except socket.error as err:
    print('%s hatadan dolayı socket olusamadi' %(err))

port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print('host çözümlenmesinde bir hata oluştu')
    sys.exit()
s.connect((host_ip,port))

print("Google baglanti basarili on port ==  %s" %(host_ip))

