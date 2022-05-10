import socket
import binascii

M_SIZE = 1024

serv_address = ('10.24.100.100', 1883)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# subscribe
topic = input('Input Topic> ')
topic_len = len(topic)

while True:
    data = input("Input Message> ") # 入力待機(サーバー側)
    msg_len = 2+len(topic)+1+len(data)
    send_len = sock.sendto(binascii.unhexlify(b'30')+msg_len.to_bytes(1, 'big')+topic_len.to_bytes(2, 'big')+topic.encode()+binascii.unhexlify(b'00')+data.encode(), serv_address)
    if data == "q":
        print('closing socket')
        sock.close()
        print('done')
        break
