#!/usr/bin/env python3
# Description : DirsPY - Directory Scanner (Python)
# Author : Koboi137 ( Backbox Indonesia )

from datetime import datetime
from time import sleep, strftime
import requests, sys, urllib3
import os, threading

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filenamenya = "dirs.txt"
file = open(filenamenya, 'r').read().split('\n')
user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

def banner():
	print(' ____  _          ______   __')
	print('|  _ \(_)_ __ ___|  _ \ \ / /')
	print("| | | | | '__/ __| |_) \ V /")
	print('| |_| | | |  \__ \  __/ | |')
	print('|____/|_|_|  |___/_|    |_|\n')
	print('Backbox Indonesia (c) 2017 - 2018\n\n')
	print('DirsPY v2.0 ( www.backboxindonesia.or.id )')

def helep():
	print('Usage : python3 dirspy.py <url> [option command]')
	print('-i <filename>   Custom file dictionary, default using file dirst.txt beside dirspy.py')
	print('EXAMPLE : python3 dirspy.py http://127.0.0.1/')

class cl:
	pink = '\033[95m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	end = '\033[0m'
	white = '\033[1m'
	under = '\033[4m'

def sizeof(num, suffix='B'):
	for unit in [' ','K','M','G','T','P','E','Z']:
		if abs(num) < 1024.0:
			return('{:>4} {}{}'.format(format(num, '.3g'), unit, suffix))
		num /= 1024.0

def rikues(line):
	alamat = str(url) + str(line)
	try:
		r = requests.get(alamat, headers = user_agent, timeout = 5, verify=False)
		num = int(len(r.text))
	except (requests.ConnectionError, requests.exceptions.Timeout, requests.exceptions.ChunkedEncodingError, IOError): sys.exit()
	status = r.status_code

	# Success
	if status == 200:
		if line == '': pass
		elif len(r.text) == leng: pass
		else: sys.stdout.write(cl.green + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num), alamat) + cl.end)
	# Redirect
	elif status == 301:
		if len(r.text) == leng: pass
		else: sys.stdout.write(cl.red + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num), alamat) + cl.end)
	#Internal server error
	elif status == 500:
		if len(r.text) == leng: pass
		else: sys.stdout.write(cl.pink + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num), alamat) + cl.end)
	# Unauthenticated
	elif status == 401:
		if len(r.text) == leng: pass
		else: sys.stdout.write(cl.yellow + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num), alamat) + cl.end)
	# Forbidden
	elif status == 403:
		if ".ht" in line: pass
		elif len(r.text) == leng: pass
		else: sys.stdout.write(cl.blue + '| {} | {} - {} | {}\n'.format(datetime.now().strftime('%H:%M:%S'), status, sizeof(num),alamat) + cl.end)

try:
	url = sys.argv[1]
	try:
		cek = requests.get(url, headers = user_agent, timeout = 5, verify = False)
		leng = len(cek.text)
	except:
		banner();
		print('ERROR : Invalid url or target is down..')
		os.system('kill -9 {}'.format(os.getpid()))
except:
	banner()
	helep()
	sys.exit()

if len(sys.argv)>1:
	try:
		argnya = sys.argv[2]
		try:
			if argnya == "-i":
				filenamenya = sys.argv[3]
				try:
					file = open(filenamenya, 'r').read().split('\n')
				except:
					banner();
					print('ERROR : Invalid filename')
					sys.exit()
		except:
			banner();
			print('ERROR : Invalid url or target is down..')
			sys.exit()
	except Exception as e:
		banner()
		helep()
		print(e)
		sys.exit()

no = 0
lcount = sum(1 for line in open('dirs.txt'))
banner()
print('Start scanning directory..')
print('===============================================================================')
print('| Time     | Info          | URL                                              |')
print('===============================================================================')
for line in file:
	try:
		t = threading.Thread(target=rikues, args=(line,))
		t.start()
		no = no + 1
		jumlah = ( no * 100 ) / lcount
		sys.stdout.flush()
		sys.stdout.write("| {} | {}% Line : {}\r".format(datetime.now().strftime('%H:%M:%S'), int(jumlah), int(no)))
		sys.stdout.flush()
	except(KeyboardInterrupt,SystemExit):
		print('\r| {} | Exiting program ...'.format(datetime.now().strftime('%H:%M:%S')))
		print('===============================================================================')
		os.system('kill -9 {}'.format(os.getpid()))

while True:
	sleep(3); cek = threading.active_count()
	if cek == 1: print('==============================================================================='); exit()
