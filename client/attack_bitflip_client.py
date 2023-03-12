from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util.number import bytes_to_long
from Crypto.Random import get_random_bytes
from binascii import unhexlify
import socket
from pwn import *
import re

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 3000))

conn.close()