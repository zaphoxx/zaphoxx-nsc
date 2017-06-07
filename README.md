# zaphoxx-nsc
<h2>nsc.py - simple python script to test inputs for the nslookup challenge (cscg)</h2>
<p>
Standart usage is with auto mode on (which means you just provide the actual host e.g. google.com and the script will add the 'X' and the md5hash for you). If you decide to turn off auto mode you will have to provide the necessary delimiter and md5hash by yourself.
</p>
<p>
usage: <code>root@HLKali:~/nslookup# python3 nsc.py -h</code>
<br>
[Status] parse input parameters
usage: nsc.py [-h] -i -r [--auto]

optional arguments: <br>
  -h, --help         show this help message and exit<br>
  -i, --labId    hacking-lab id - This refers to the server id from the<br>
                     created docker of the challenge.<br>
  -r, --request  actual request portion e.g. REQUESTXMD5HASH<br>
  --auto             turn auto md5 hash calculation on/off. send request<br>
                     manually.<br>
</p>
<br><br>
<h4>example (auto mode on)</h4>
<br>
<p>
<code>root@HLKali:~/nslookup# python3 nsc.py -i aa0141e6e79c -r 'chroot'</code>
<br>
<p>
[Status] parse input parameters<br>
[+] labid: aa0141e6e79c<br>
[+] request: chroot<br>
[+] md5hash: 466673de471fac1f97ef0cac4eb9a272<br>
[+] target: aa0141e6e79c.i.hacking-lab.com<br>
[STATUS] Connect to target 'aa0141e6e79c.i.hacking-lab.com'<br>
[+] host=chrootX466673de471fac1f97ef0cac4eb9a272<br>
[CONNECTION] 200 - OK<br>
[+] RESPONSE HEADERS<br>
	[+] Date : Sat, 20 May 2017 19:04:10 GMT<br>
	[+] Server : Apache/2.4.18 (Ubuntu)<br>
	[+] Vary : Accept-Encoding<br>
	[+] Content-Encoding : gzip<br>
	[+] Content-Length : 532<br>
	[+] Keep-Alive : timeout=5, max=100<br>
	[+] Connection : Keep-Alive<br>
	[+] Content-Type : text/html; charset=UTF-8<br>
[+] ------------------------------------------<br>
</code>
<code>
<verbatim>
b'\n<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<meta charset="utf-8" />\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    \t<title>Online NS Lookup</title>\n    \t<link rel="stylesheet" href="style.css" />\n\t</head>\n\n\t<body>\n\n\t\t<div class="middle">\n\t\t\t<h1>Welcome to Online NS Lookup</h1>\n\n\t\t\t<p>Please choose a domain</p>\n\n\t\t\t    <form method="post">\n\t\t\t\t  <select name="host">\n\t\t\t\t  <option value=\'google.comX1d5920f4b44b27a802bd77c4f0536f5a\'>google.com</option><option value=\'yahoo.comX50cd1a9a183758039b0841aa738c3f0b\'>yahoo.com</option><option value=\'ch.chX1207e86643deca2eb8fc69dc5e8aeb2b\'>ch.ch</option>\t\t\t\t   </select>\n\t\t\t      <input type="submit">\n\t\t\t    </form>\n\n\t\t\t\t\t\t\t<p class="result">Result</p>\n\t\t\t\t<p>\n        nicetry.com        </p>\n\t\t\t\n\t\t</div>\n\n\n    <footer>\n      Thanks to: wgEt, tAr, .NETst@t and chR00t!\n    </footer>\n\t</body>\n</html>\n'<br>
[+] ------------------------------------------<br>
[fail] nice try!<br>
</verbatim></code>
<br><hr><br>
<h4>example (auto mode off)</hr>
<br><br>
<code>
root@HLKali:~/nslookup# python3 nsc.py -i aa0141e6e79c -r 'google.net' --auto
</code>
<code><verbatim>
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
</verbatim></code>
