import socket
import binascii

M_SIZE = 1024

serv_address = ('10.24.100.100', 1883)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# subscribe
topic = input('Input Topic> ')
msg_len = 2+len(topic)+1 
topic_len = len(topic)
send_len = sock.sendto(binascii.unhexlify(b'82')+msg_len.to_bytes(1, 'big')+topic_len.to_bytes(2, 'big')+topic.encode()+binascii.unhexlify(b'00'), serv_address)
# recv suback
rx_message, addr = sock.recvfrom(M_SIZE)
#print(rx_message)
if rx_message[0:1] == b'\x80':
	print("SUBSCRIBE SUCCESS")

while True:
	rx_meesage, addr = sock.recvfrom(M_SIZE)
	rx_meesage = rx_meesage[4:]
	for i in range(len(rx_message)):
		if rx_meesage[i:i+1]==b'\x00':
			index = i+1
			break
	rx_meesage = rx_meesage[index:]
	print("message: ", rx_meesage.decode())
	if rx_meesage == b'q':             # qが押されたら終了
		sock.close()
		print('done')
		break