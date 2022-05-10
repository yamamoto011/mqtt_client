import socket
import binascii

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("10.24.100.102", 1883))

# subscribe: 800c0004 + topic: 686f676500(hoge)
data = input("Subscribe Topic>") # 入力待機
msg_len = 2+len(data)+1 
soc.send(binascii.unhexlify(b'82')+msg_len.to_bytes(1, 'big')+binascii.unhexlify('0004')+data.encode()+binascii.unhexlify(b'00'))
msg = soc.recv(1024)
if msg[0:1]==b'\x90':
    print("SUBSCRIBE SUCCESS")

while(1):
    msg = soc.recv(1024)
    msg = msg[4:]
    for i in range(len(msg)):
        if msg[i:i+1]==b'\x00':
            index = i+1
            break
    msg = msg[index:]
    # msg = bytes.fromhex(msg.decode("utf-8")).decode('utf-8')
    print("message: ", msg.decode()) 
    if msg == b'q':             # qが押されたら終了
        soc.close()
        break
soc.close()
