#!/usr/bin/env python2
# -*- coding: iso-8859-1 -*-

from datetime import datetime
from threading import Thread
from time import sleep, strftime
from IPython.display import clear_output
import requests, sys

file = open('dirs.txt', 'r').read().split('\n')
user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

def banner():
	print """
 ____  _          ______   __
|  _ \(_)_ __ ___|  _ \ \ / /
| | | | | '__/ __| |_) \ V /
| |_| | | |  \__ \  __/ | |
|____/|_|_|  |___/_|    |_|

Copyright © 2017 - Backbox Indonesia
"""

def helep():
	print "DirsPY v1.1 ( www.backboxindonesia.or.id )"
	print "Usage : python2 dirspy.py <url>"
	print "EXAMPLE : python2 dirspy.py http://127.0.0.1/"

class cl:
	pink = '\033[95m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	end = '\033[0m'
	white = '\033[1m'
	under = '\033[4m'

def rikues(line):
	alamat = str(url) + str(line)
	try: r = requests.get(alamat, headers = user_agent, timeout = 5)
	except (requests.ConnectionError, requests.exceptions.Timeout): sys.exit()
	status = r.status_code

	if status == 200:
		if line == '': pass
		else: print cl.green + '[{2}] {1} - {0}'.format(alamat, status, datetime.now().strftime('%H:%M:%S')) + cl.end
	elif status == 301:
		print cl.red + '[{2}] {1} - {0}'.format(alamat, status, datetime.now().strftime('%H:%M:%S')) + cl.end
	elif status == 500:
		print cl.pink + '[{2}] {1} - {0}'.format(alamat, status, datetime.now().strftime('%H:%M:%S')) + cl.end
	elif status == 401:
		print cl.yellow + '[{2}] {1} - {0}'.format(alamat, status, datetime.now().strftime('%H:%M:%S')) + cl.end
	elif status == 403:
		if ".ht" in line: pass
		else: print cl.blue + '[{2}] {1} - {0}'.format(alamat, status, datetime.now().strftime('%H:%M:%S')) + cl.end

try: url = sys.argv[1]
except: 
	banner()
	helep()
	sys.exit()

no = 0
lcount = sum(1 for line in open('dirs.txt'))
banner()
print "Start scanning directory.."
for line in file:
	try:
		t = Thread(target=rikues, args=(line,))
		t.start()
		no = no + 1
		jumlah = ( no * 100 ) / lcount
		sys.stdout.flush()
		sys.stdout.write("[{}] => {}% Line : {}\r".format(datetime.now().strftime('%H:%M:%S'), jumlah, no))
	except(KeyboardInterrupt,SystemExit): break

sleep(1)
print "\n\nScanning compleated.."
