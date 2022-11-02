import socket
import sys
import uuid
from time import sleep

HOST = sys.argv[1]
PORT = int(sys.argv[2])
UUID = str(uuid.uuid4())

def Client():
	host = HOST
	port = PORT

	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((host,port))

	client_uuid = UUID
	#keep connection alive
	while True:
		sock.send(client_uuid.encode('ascii'))
		data = sock.recv(4096)

		print("my id is: " + UUID)
		print('Received from the server :',str(data.decode('ascii')))
		sleep(0.1)


if __name__ == '__main__':
	Client()
