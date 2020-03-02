import socket
import string
import binascii

HOST = "ec2-15-188-238-135.eu-west-3.compute.amazonaws.com"
PORT = 3000
CHARSET = string.ascii_letters + string.digits

def get_block_size(self):
    return 16

def guess_max_size_secret(self):
    return 9

def break_it(self):
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
                if len(secret) == max_size_secret:
                    return secret
        except Exception as e:
            print(e)


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
