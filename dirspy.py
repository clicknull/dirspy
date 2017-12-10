# -*- coding: iso-8859-1 -*-
from datetime import datetime
import requests

time = datetime.now().strftime('%H:%M:%S')
file = open('dirs.txt', 'r').read().split('\n')
url = "http://127.0.0.1:8000/"
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
	blue = '\033[94m'
	green = '\033[92m'
	red = '\033[91m'
	end = '\033[0m'

print "Start scanning directory.."
for line in file:
	alamat = str(url) + str(line)
	r = requests.get(alamat, headers = user_agent)
	status = r.status_code
	if status == 200:
		print cl.green + '[{2}] {1} - {0}'.format(alamat, status, time) + cl.end
	elif status == 500:
		print cl.blue + '[{2}] {1} - {0}'.format(alamat, status, time) + cl.end
	elif status == 403:
		print cl.red + '[{2}] {1} - {0}'.format(alamat, status, time) + cl.end
	elif not file:
		break

print "\nScanning compleated.."
