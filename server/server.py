import socket
from time import sleep
from _thread import *

PORT = 80
def threaded(c):
	while True:

		# data received from client
		data = c.recv(4096)
		if not data:
			print('Bye')
			
			# lock released on exit
			#print_lock.release()
			break
		# send back reversed string to client
		print("client: " + str(data.decode('ascii')))
		c.send(data)

	# connection closed
	c.close()


def Server():
	host = socket.gethostname()

	port = PORT
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host, port))
	print("socket binded to port", port)

	# put the socket into listening mode
	sock.listen(50)
	print("socket is listening")

	# a forever loop until client wants to exit
	while True:

		# establish connection with client
		c, addr = sock.accept()

		# lock acquired by client
		#print_lock.acquire()
		print('Connected to :', addr[0], ':', addr[1])

		# Start a new thread and return its identifier
		start_new_thread(threaded, (c,))


if __name__ == '__main__':
	Server()
