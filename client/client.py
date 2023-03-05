import socket
import sys

def send_msg(s, msg):
        enc = msg.encode()
        s.send(enc)

if len(sys.argv) != 2:
    print("Usage: %s <ip_address>\n" % (sys.argv[0]))
    sys.exit()

server = sys.argv[1]
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))

#s.send("test")
response = s.recv(4096)
print(response)
response = s.recv(4096)
print(response)
send_msg(s, 'user123')
response = s.recv(4096)
print(response)
send_msg(s, 'goBigDawgs123')
response = s.recv(4096)
print(response)