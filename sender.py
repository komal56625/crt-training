import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add="192.168.130.1"
port=786
complete=(ip_add,port)
message=input(" write meaagae")
encode_msg=message.encode("ascii")
s.sendto(encode_msg,complete)
