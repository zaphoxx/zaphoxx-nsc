#!/usr/bin/python3

import argparse
import http.client
import urllib.parse
import hashlib
import base64
import gzip
import re
import html

__gParameters={}

def main():
	# argument parser
	print("[Status] parse input parameters")
	args=initParser()
	connection=connectTarget()
	sendRequest(connection);
	connection.close()

def initParser():
	parser=argparse.ArgumentParser()
	parser.add_argument("-i","--labId",metavar="\b",dest="labId",required=True,help="hacking-lab id - This refers to the server id from the created docker of the challenge.")
	parser.add_argument("-r","--request",metavar="\b",dest="req",required=True,help="actual request portion e.g. <req>X<md5hash>")
	parser.add_argument("--auto",dest="auto",action="store_false",required=False,help="turn auto md5 hash calculation on/off. send request manually.")
	parser.set_defaults(auto=True)
	args=parser.parse_args()
	handleArgs(args)

def handleArgs(args):
	# handle commandline arguments
	global __gParameters
	target="{}.i.hacking-lab.com".format(args.labId)
	md5hash=hashlib.md5((args.req).encode('utf-8')).hexdigest()
	reqFull=""
	if args.auto:
		reqFull="{}X{}".format(args.req,md5hash)
	else:
		reqFull=args.req

	__gParameters={'labId':args.labId,
				'request':args.req,
				'target':target,
				'md5hash':md5hash,
				'reqFull':reqFull}
	print("[+] labid: {}\n[+] request: {}\n[+] md5hash: {}\n[+] target: {}".format(__gParameters['labId'],__gParameters['request'],__gParameters['md5hash'],__gParameters['target']))
	return __gParameters

def connectTarget():
	# connect to target
	print("[STATUS] Connect to target '{}'".format(__gParameters['target']))
	try:
		connection = http.client.HTTPConnection(__gParameters['target'])
	except Exception as e1:
		print("[!!!] Could not establish connection in function connectTarget()!")
		try:
			connection.close()
		except Exception as e2:
			print("[!!!] Could not close connection in function connectTarget()!")
			exit(0)
	return connection

'''
Host: 424d99fe5baa.i.hacking-lab.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 48
Referer: http://424d99fe5baa.i.hacking-lab.com/
Connection: keep-alive
Upgrade-Insecure-Requests: 1
'''

def sendRequest(connection):
	param={"host":"{}".format(__gParameters['reqFull'])}
	requestParameters=urllib.parse.urlencode(param)
	print("[+] {}".format(requestParameters))
	header={"Host":__gParameters['target'],
			"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0",
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Language":"en-US,en;q=0.5",
			"Accept-Encoding":"gzip, deflate",
			"Referer":"http://{}".format(__gParameters['target']),
			"Connection":"keep-alive",
			"Upgrade-Insecure-Requests":1,
			"Content-Type":"application/x-www-form-urlencoded",
			"Content-Length":len(urllib.parse.quote_plus(__gParameters['reqFull']))+len("host=")
			}
	try:
		connection.request("POST","/",requestParameters,header)
		resp=connection.getresponse()
	except Exception as e3:
		print("[-] Error sending request! Exit(0)")
		print(e3)
		exit(0)

	print("[CONNECTION] {} - {}".format(resp.status,resp.reason))
	data=resp.read()
	try:
		dataOut=gzip.decompress(data)
	except:
		dataOut=data
		pass
	# --------- delete content below this line -----------
	#if str(data).find("shiny")>-1:
	#	fail=False
	# --------- delete content above this line -----------
	print("[+] RESPONSE HEADERS")
	status="[success]"
	for key in resp.headers:
		print("\t"+"[+] "+key+" : "+resp.headers[key])
		if key=="Location" and resp.headers[key]=="error.html":
			status="[fail] Don't manipulate my website!"
	print("[+] ------------------------------------------")
	print(str(dataOut))
	print("[+] ------------------------------------------")
	if("nicetry.com" in str(dataOut)):
		status="[fail] nice try!"

	print(status)

	connection.close()

if __name__=="__main__":
	main()
