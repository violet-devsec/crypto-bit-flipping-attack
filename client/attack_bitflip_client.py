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

xor = ord('r') ^ ord('s')

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 3000))

print(conn.recv(4096))
print(conn.recv(4096))
send_msg(conn, 'admin&parsword=goBigDawgs123\r\n')
print(conn.recv(4096))
send_msg(conn, '\r\n')

l_cipher = conn.recv(4096).decode()
print(l_cipher)
match = re.match(r'Leaked ciphertext: (.+)', l_cipher)
print('Ciphertext:', match[1])

cipher = match[1]
cipher = cipher[:16] + hex(int(cipher[16:18],16) ^ xor)[2:] + cipher[18:]
print('Modified Ciphertext', cipher)

print()
send_msg(conn, cipher + '\r\n')
print(conn.recv(4096))

conn.close()