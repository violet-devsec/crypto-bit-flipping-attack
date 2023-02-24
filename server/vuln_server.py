import socketserver
import socket, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from binascii import unhexlify
from secret import FLAG

def send_msg(s, msg):
    enc = msg.encode()
    s.send(enc)

def main(s):
    send_msg(s, wlcm_msg)
    print('### Server started! ###')

    send_msg(s, 'username: ')
    user = s.recv(4096).decode().strip()

    send_msg(s, user +"'s password: ")
    passwd = s.recv(4096).decode().strip()

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_resuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 3000), TaskHandler)
    server.serve_forever()