import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5020
number = "5"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", number

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(number, (UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "\n\nResult of factorial is", data
