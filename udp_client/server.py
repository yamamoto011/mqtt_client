import socket
import time

M_SIZE = 1024

# 
host = '127.0.0.1'
port = 8890

locaddr = (host, port)

# ??????????
sock = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
print('create socket')

# ??????????IP?????????????
sock.bind(locaddr)

while True:
    try :
        # ?Client???message?????
        print('Waiting message')
        message, cli_addr = sock.recvfrom(M_SIZE)
        message = message.decode(encoding='utf-8')
        print(f'Received message is [{message}]')

        # Client??????????????
        time.sleep(1)

        # ?Client?????message???
        print('Send response to Client')
        sock.sendto('Success to receive message'.encode(encoding='utf-8'), cli_addr)

    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()
        break
