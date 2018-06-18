import socket

hostname = 'localhost'
port = 12000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((hostname, port))
print('start server')
try:
    while True:
        message, client_address = s.recvfrom(2048)
        print('received message', message)
        print('client address', client_address)
        s.sendto(message, client_address)
except Exception:
    pass
finally:
    s.close()

print('stop server')

