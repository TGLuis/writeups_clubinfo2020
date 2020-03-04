import socket
import string
import binascii
import struct

HOST = "ec2-15-188-238-135.eu-west-3.compute.amazonaws.com"
PORT = 3000
CHARSET = string.ascii_letters + string.digits

def get_block_size():
    return 16

def guess_max_size_secret():
    return 16

def break_it():
    print("break it")
    while True:
        max_size_secret = guess_max_size_secret()
        try:
            secret = ""
            for size in range((max_size_secret - 1), -1, -1):
                origin = "A" * size
                origin_response = send_and_receive(origin)

                tmp = "A" * size + secret
                for character in CHARSET:
                    tmp_response = send_and_receive(tmp + character)

                    if origin_response[:max_size_secret] == tmp_response[:max_size_secret]:
                        print("secret add char: ", character)
                        secret += character
                        break
                if len(secret) == 9:
                    return secret
        except Exception as e:
            print(e)

def recvall(sock, n):
    data = b''
    addr = None
    while len(data) < n:
        packet, addr = sock.recvfrom(n - len(data))
        if not packet:
            return None
        data += packet
    return data, addr

def send_msg_to_oracle(sock, msg):
    msg = struct.pack('>I', len(msg)) + msg.encode("utf-8")
    res = sock.sendall(msg)
    if not res:
        return len(msg)

def recv_msg(sock):
    raw_msglen, _ = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    return recvall(sock, msglen)

def send_and_receive(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        # pre processing to do for the value to remove it!!
        msg = "a"*9 + msg
        resp = send_to_oracle(sock, msg)
        resp = resp[32:]
        return resp

def send_to_oracle(sock, msg):
    send_msg_to_oracle(sock, msg)
    out, _ = recv_msg(sock)
    return out

print(break_it())
