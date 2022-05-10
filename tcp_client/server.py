# -*- coding: utf-8 -*-
import socket
import binascii


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 50007))    # 指定したホスト(IP)とポートをソケットに設定
s.listen(1)                     # 1つの接続要求を待つ
soc, addr = s.accept()          # 要求が来るまでブロック
print("Conneted by"+str(addr))  #サーバ側の合図

# receive subscribe 
# topic: hoge
data = soc.recv(1024)       # データを受信（1024バイトまで）
print("Client>", data)       # サーバー側の書き込みを表示

topic = input("Publish Topic>") # 入力待機(サーバー側)


while (1):
    #publish
    data = input("Message>") # 入力待機(サーバー側)
    soc.send(binascii.unhexlify(b'300c0004')+topic.encode()+binascii.unhexlify(b'00')+data.encode())              # ソケットにデータを送信
    if data == "q":             # qが押されたら終了
        soc.send(bytes(data, 'utf-8'))
        soc.close()
        break
soc.close()