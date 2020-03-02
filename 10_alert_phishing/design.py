from subprocess import Popen, PIPE
import argparse
import binascii
import string
import struct
import socket

def send_msg_to_oracle(sock, msg):
    msg = struct.pack('>I', len(msg)) + msg.encode("utf-8")
    res = sock.sendall(msg)
    if not res:
        return len(msg)

def display_byte(data):
    print(binascii.b2a_hex(data).decode("utf-8"))

def recvall(sock, n):
    data = b''
    addr = None
    while len(data) < n:
        packet, addr = sock.recvfrom(n - len(data))
        if not packet:
            return None
        data += packet
    return data, addr

def recv_msg(sock):
    raw_msglen, _ = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    return recvall(sock, msglen)

def send_to_oracle(sock, msg):
    send_msg_to_oracle(sock, msg)
    out, _ = recv_msg(sock)
    return out

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", action="store", dest="ip", default="ec2-15-188-238-135.eu-west-3.compute.amazonaws.com")
    parser.add_argument("--port", type=int, action="store", dest="port", default=3000)

    args = parser.parse_args()
    message = "a"*1000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((args.ip, args.port))
        resp = send_to_oracle(sock, 1000*"a" )
        print("\tlen message = ", 1000, "\tlen = ", len(resp))
        display_byte(resp)
    
    for i in range(0,100,5):
        mes = i*"a"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((args.ip, args.port))
            resp = send_to_oracle(sock, mes )
            print("i = ", i, "\tlen message = ", len(mes), "\tlen = ", len(resp))
            #display_byte(resp)

