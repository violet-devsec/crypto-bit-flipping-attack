import socketserver
import socket, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from binascii import unhexlify
#from secret import FLAG

wlcm_msg = '##################  Welcome ####################'

FLAG = '{YOU_ARE_BITFLIP_SERVER_NOW}'

key = get_random_bytes(16)
iv  = get_random_bytes(16)

def send_msg(s, msg):
    enc = msg.encode()
    s.send(enc)

def encrypt_data(data):
    padded = pad(data.encode(), 16, style='pkcs7')
    cipher= AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(padded)
    return enc.hex()

def decrypt_data(encryptedParams):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    paddedParams = cipher.decrypt(unhexlify(encryptedParams))
    print(paddedParams)
    if b'admin&password=goBigDawgs123' in unpad(paddedParams,16,style='pkcs7'):
        return 1
    else:
        return 0

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

    if check:
        send_msg(s, 'Logged in successfully!\nYour flag is: ' + FLAG)
        s.close()
    else:
        send_msg(s, 'Please try again.'+'\n')
        s.close()

class TaskHandler(socketserver.BaseRequestHandler):
    def handle(self):
        main(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_resuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 3000), TaskHandler)
    server.serve_forever()