import socket

host = "127.0.0.1"

for port in range(1,65535):
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = client_socket.connect_ex((host, port))
	client_socket.close()
	if(result == 0):
		print(str(port)+" Port is Open")

