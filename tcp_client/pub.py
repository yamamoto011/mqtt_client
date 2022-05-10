# -*- coding: utf-8 -*-
import socket
import binascii


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("10.24.100.102", 1883))

# receive subscribe 
# topic: hoge
topic = input("Publish Topic>")

while (1):
    #publish
    data = input("Publish Message>") # 入力待機(サーバー側)
    msg_len = 2+len(topic)+1+len(data)
    soc.send(binascii.unhexlify(b'30')+msg_len.to_bytes(1, 'big')+binascii.unhexlify('0004')+topic.encode()+binascii.unhexlify(b'00')+data.encode())              # ソケットにデータを送信
    if data == "q":             # qが押されたら終了
        soc.send(bytes(data, 'utf-8'))
        soc.close()
        break
soc.close()
