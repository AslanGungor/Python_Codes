# Python_Codes

Socket creation:

int sockfd = socket(domain, type, protocol)

sockfd: socket descriptor, an integer (like a file-handle)

domain: integer, communication domain e.g., AF_INET (IPv4 protocol) , AF_INET6 (IPv6 protocol)

type: communication type
SOCK_STREAM: TCP(reliable, connection oriented)
SOCK_DGRAM: UDP(unreliable, connectionless)

protocol: Protocol value for Internet Protocol(IP), which is 0. 
          This is the same number which appears on protocol field in the IP header of a packet.(man protocols for more details)

'.whl' DOSYALARINI YÜKLEMEK

'C:\Users(user)\AppData\Local\Programs\Python\Python35\Scripts' konumuna eklentiyi atıp 
pip install .whl


