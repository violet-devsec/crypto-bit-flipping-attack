from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util.number import bytes_to_long
from Crypto.Random import get_random_bytes
from binascii import unhexlify
import socket
from pwn import *
import re

def send_msg(s, msg):
        enc = msg.encode()
        s.send(enc)

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 3000))

print(conn.recv(4096))
print(conn.recv(4096))
send_msg(conn, 'admin&parsword=goBigDawgs123\r\n')
print(conn.recv(4096))
send_msg(conn, '\r\n')

conn.close()