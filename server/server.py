from colorama import Fore, Back, Style, init
from socket   import socket, AF_INET, SOCK_STREAM
from json     import load, dump
from os       import exists

init()


FNAME = 'data.json'

if not exists(FNAME): users_data = {}
else:
	with open(FNAME, 'r') as file: users_data = load(file)


LHOST = '127.0.0.1'
LPORT = 7777
CHSZ  = 1024

HEADER_LEN = 4


with socket(AF_INET, SOCK_STREAM) as sock:

	sock.bind((HOST, PORT))

	print(f'[LISTENING]\tOn {LHOST}:{LPORT}')
	sock.listen()

	conn, addr = sock.accept()
	print(f'[CONN]\tConnected by {addr}. Receiving data.')

	if addr not in users_data:
		print(f'[WARN]\tAn unknown peer ({addr}) trying to connect. Please, bind in before collecting data from it. Aborting.')
		sock.close()
		exit(0)

	chunks = []

	with conn:
		while True:
			chunk = conn.recv(CHSZ)
			if not chunk:
				print(f'[ERROR]\tNo data received from {addr}. Aborting.')
				break
			chunks.append(chunk)

		data = bytes.join(chunks)
		task_number = int.from_bytes(data[:HEADER_LEN], 'big')	# int
		task_answer = data[HEADER_LEN:].decode('utf-8')			# str
		print(f'New data received:\n\tAddress:\t{addr}\n\tPeer name:\t{name}\n\tTask number:\t{task_number}\n\tTask answer:\t{task_answer}\n')

		users_data[addr]['number'] = task_number
		users_data[addr]['answer'] = task_answer

		with open(FNAME, 'w') as file: dump(users_data, file)