import socket

hostname = 'localhost'
port = 12000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(input('write your message here...\n').encode(), (hostname, port))
message, server_address = s.recvfrom(2048)
print('message', message)
print('address of server', server_address)
s.close()

