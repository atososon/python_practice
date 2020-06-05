from datetime import datetime
import socket
server_address = ('localhost', 6789)
max_size = 4096
print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)
date, client = server.recvfrom(max_size)
print('At', datetime.now(), client, 'said', date)

if date == b'time':
    now = datetime.now()
    now_iso = now.isoformat()
    nowcode = now_iso.encode('utf-8')
    server.sendto(nowcode, client)
server.close()