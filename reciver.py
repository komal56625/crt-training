import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add="192.168.130.1"
port=786
complete=(ip_add,port)
s.bind(complete)
while True:
    message=s.recvfrom(1024)
    message=message[0].decode('ascii')
    print(message)