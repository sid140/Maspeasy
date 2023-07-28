#!/usr/bin/env python3

import subprocess
import argparse

print("Welcome to Mapeasy, a simple dumbdown custom version of Nmap. Developed by Xalt\n Please run proxychains by typing proxynow command before using othe commands in the help section")
try:
	parser = argparse.ArgumentParser(description="nmap made easy")
	parser.add_argument("--SYNSCAN", action="store_true", help="This is a TCP SYN SCAN, also known as a stealth scan.")
	parser.add_argument("--TwSCAN", action="store_true", help="The -sT scan is more accurate than a -sS scan, but the downside is that it is slower, makes more noise and easily detected by well set-up firewalls.")
	parser.add_argument("--UDPSCAN", action="store_true", help="This scan is used to scan for UDP ports.")
	parser.add_argument("--FASTPING", action="store_true", help="This is a simple and fast ping scan to see which hosts reply to ICMP ping packets.")
	parser.add_argument("--VERSCAN", action="store_true", help="This is a service version scan. In order to know what exploits will work")
	parser.add_argument("--proxynow", action="store_true", help="This will install proxychains and tor")
	args = parser.parse_args()
	user_input = input("Enter the IP address: ")
	
except ChildProcessError:
	print("OPeration not working..Exiting")
	raise e

def proxynow():
subprocess.run(["sudo", "apt-get", "-o", "Acquire::http::Proxy=http://localhost:9050", "update"], check=True)
subprocess.run(["sudo", "apt-get", "-o", "Acquire::http::Proxy=http://localhost:9050", "install", "proxychains"], check=True)


if args.SYNSCAN:
    subprocess.run(["proxychains","nmap", "-sS", user_input], check=True)

if args.TwSCAN:
	subprocess.run(["proxychains","nmap", "-sn", user_input], check=True)
	

if args.UDPSCAN:
	subprocess.run(["proxychains","nmap", "-sU", user_input], check=True)

if args.FASTPING:
	subprocess.run(["proxychains","nmap", "-sn", user_input], check=True)

if args.VERSCAN:
	subprocess.run(["proxychains","nmap", "-sV", user_input], check=True)

if args.proxynow:
	proxynow()



