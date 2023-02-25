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

    msg = 'logged_username=' + user + '&password=' + passwd

    try:
        assert('admin&password=goBigDawgs123' not in msg)
    except AssertionError:
        send_msg(s, 'You cannot login as an admin from an external IP. Good bye!')
        raise

    send_msg(s, "Leaked ciphertext: " + encrypt_data(msg)+'\n')
    send_msg(s, "Enter ciphertext: ")

    enc_msg = s.recv(4096).decode().strip()
    check = False

    try:
        check = decrypt_data(enc_msg)
    except Exception as e:
        send_msg(s, str(e) + '\n')
        s.close()

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_resuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 3000), TaskHandler)
    server.serve_forever()