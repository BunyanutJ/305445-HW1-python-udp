import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5020
summation = 1

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    n = int(data)
    print "Number:", n
    while n>0:
        summation = summation*n
        n=n-1
    print "Result :", summation
    s = str(summation)
    sock.sendto(s, addr)
