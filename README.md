# zaphoxx-nsc
nsc.py - simple python script to test inputs for the nslookup challenge (cscg).

Standart usage is with auto mode on (which means you just provide the actual host e.g. google.com and the script will add the 'X' and the md5hash for you). If you decide to turn off auto mode you will have to provide the necessary delimiter and md5hash by yourself.


usage:
root@HLKali:~/nslookup# python3 nsc.py -h
[Status] parse input parameters
usage: nsc.py [-h] -i -r [--auto]

optional arguments:
  -h, --help         show this help message and exit
  -i, --labId    hacking-lab id - This refers to the server id from the
                     created docker of the challenge.
  -r, --request  actual request portion e.g. <req>X<md5hash>
  --auto             turn auto md5 hash calculation on/off. send request
                     manually.


example (auto mode on):

root@HLKali:~/nslookup# python3 nsc.py -i aa0141e6e79c -r 'chroot'
<code>
[Status] parse input parameters
[+] labid: aa0141e6e79c
[+] request: chroot
[+] md5hash: 466673de471fac1f97ef0cac4eb9a272
[+] target: aa0141e6e79c.i.hacking-lab.com
[STATUS] Connect to target 'aa0141e6e79c.i.hacking-lab.com'
[+] host=chrootX466673de471fac1f97ef0cac4eb9a272
[CONNECTION] 200 - OK
[+] RESPONSE HEADERS
	[+] Date : Sat, 20 May 2017 19:04:10 GMT
	[+] Server : Apache/2.4.18 (Ubuntu)
	[+] Vary : Accept-Encoding
	[+] Content-Encoding : gzip
	[+] Content-Length : 532
	[+] Keep-Alive : timeout=5, max=100
	[+] Connection : Keep-Alive
	[+] Content-Type : text/html; charset=UTF-8
[+] ------------------------------------------
b'\n<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<meta charset="utf-8" />\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    \t<title>Online NS Lookup</title>\n    \t<link rel="stylesheet" href="style.css" />\n\t</head>\n\n\t<body>\n\n\t\t<div class="middle">\n\t\t\t<h1>Welcome to Online NS Lookup</h1>\n\n\t\t\t<p>Please choose a domain</p>\n\n\t\t\t    <form method="post">\n\t\t\t\t  <select name="host">\n\t\t\t\t  <option value=\'google.comX1d5920f4b44b27a802bd77c4f0536f5a\'>google.com</option><option value=\'yahoo.comX50cd1a9a183758039b0841aa738c3f0b\'>yahoo.com</option><option value=\'ch.chX1207e86643deca2eb8fc69dc5e8aeb2b\'>ch.ch</option>\t\t\t\t   </select>\n\t\t\t      <input type="submit">\n\t\t\t    </form>\n\n\t\t\t\t\t\t\t<p class="result">Result</p>\n\t\t\t\t<p>\n        nicetry.com        </p>\n\t\t\t\n\t\t</div>\n\n\n    <footer>\n      Thanks to: wgEt, tAr, .NETst@t and chR00t!\n    </footer>\n\t</body>\n</html>\n'
[+] ------------------------------------------
[fail] nice try!
</code>
example (auto mode off):

root@HLKali:~/nslookup# python3 nsc.py -i aa0141e6e79c -r 'google.net' --auto
<code>
[Status] parse input parameters
[+] labid: aa0141e6e79c
[+] request: google.net
[+] md5hash: 21a352716c73a45f962bb49474057ca0
[+] target: aa0141e6e79c.i.hacking-lab.com
[STATUS] Connect to target 'aa0141e6e79c.i.hacking-lab.com'
[+] host=google.net
[CONNECTION] 302 - Found
[+] RESPONSE HEADERS
	[+] Date : Sat, 20 May 2017 19:11:32 GMT
	[+] Server : Apache/2.4.18 (Ubuntu)
	[+] Location : error.html
	[+] Content-Length : 0
	[+] Keep-Alive : timeout=5, max=100
	[+] Connection : Keep-Alive
	[+] Content-Type : text/html; charset=UTF-8
[+] ------------------------------------------
b''
[+] ------------------------------------------
[fail] Don't manipulate my website!
</code>
