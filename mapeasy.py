#!/usr/bin/env python3

import subprocess
import argparse

print("Welcome to Mapeasy, a simple dumbdown custom version of Nmap. Developed by Sid140")
try:
	parser = argparse.ArgumentParser(description="nmap made easy")
	parser.add_argument("--SYNSCAN", action="store_true", help="This is a TCP SYN SCAN, also known as a stealth scan.")
	parser.add_argument("--TwSCAN", action="store_true", help="The -sT scan is more accurate than a -sS scan, but the downside is that it is slower, makes more noise and easily detected by well set-up firewalls.")
	parser.add_argument("--UDPSCAN", action="store_true", help="This scan is used to scan for UDP ports.")
	parser.add_argument("--FASTPING", action="store_true", help="This is a simple and fast ping scan to see which hosts reply to ICMP ping packets.")
	parser.add_argument("--VERSCAN", action="store_true", help="This is a service version scan. In order to know what exploits will work")
	args = parser.parse_args()
	user_input = input("Enter the IP address: ")
except ChildProcessError:
	print("OPeration not working..Exiting")
	raise e


if args.SYNSCAN:
    subprocess.run(["nmap", "-sS", user_input], check=True)

if args.TwSCAN:
	subprocess.run(["nmap", "-sn", user_input], check=True)
	

if args.UDPSCAN:
	subprocess.run(["nmap", "-sU", user_input], check=True)

if args.FASTPING:
	subprocess.run(["nmap", "-sn", user_input], check=True)

if args.VERSCAN:
	subprocess.run(["nmap", "-sV", user_input], check=True)
