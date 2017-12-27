# -*- coding: iso-8859-1 -*-
from datetime import datetime
from threading import Thread
from time import sleep as ts
import requests

time = datetime.now().strftime('%H:%M:%S')
file = open('dir.txt', 'r').read().split('\n')
url = "http://fadil.bnet.id/"
user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

print """
 ____  _          ______   __
|  _ \(_)_ __ ___|  _ \ \ / /
| | | | | '__/ __| |_) \ V /
| |_| | | |  \__ \  __/ | |
|____/|_|_|  |___/_|    |_|

Copyright © 2017 - Backbox Indonesia
"""

class cl:
	pink = '\033[95m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	end = '\033[0m'
	white = '\033[1m'
	under = '\033[4m'

print "Start scanning directory.."

def rikues(line):
	alamat = str(url) + str(line)
	r = requests.get(alamat, headers = user_agent, timeout = 5)
	status = r.status_code
	if status == 200:
		print cl.green + '[{2}] {1} - {0}'.format(alamat, status, time) + cl.end
	elif status == 301:
		print cl.red + '[{2}] {1} - {0}'.format(alamat, status, time) + cl.end
	elif status == 500:
		print cl.pink + '[{2}] {1} - {0}'.format(alamat, status, time) + cl.end
	elif status == 401:
		print cl.yellow + '[{2}] {1} - {0}'.format(alamat, status, time) + cl.end
	elif status == 403:
		if ".ht" in line: pass
		else: print cl.blue + '[{2}] {1} - {0}'.format(alamat, status, time) + cl.end

for line in file:
	try:
		t = Thread(target=rikues, args=(line,))
		t.start()
	except(KeyboardInterrupt,SystemExit): break

ts(1)
print "\nScanning compleated.."
