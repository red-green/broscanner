## BroScanner:
## streaming python data analyzer for the bro network analyzer

import os, sys
import tailer
import time
import json

from config import *
import bparser


## simple alert notifier:
'''
import notifiers
for i in bparser.parseentries('notice.log'):
	print i
	notifiers.notify(i['msg'])
'''

## simple json parser
for i in bparser.parseentries(sys.argv[1]):
	print json.dumps(i)
