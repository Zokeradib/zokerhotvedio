import os 
import time 
import sys
#------color------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
#------linecolor def-----#
def x():
	print(43*'\033[1;33m=')
def sex():
	print(43*'\033[1;36m=')
def line():
	print(43*'\033[1;37m-')
#----logo----#

adiib=("""
┏━━━┓┏━━━┓┏━━┓┏━━┓────┏━┓┏━┓ 
┃┏━┓┃┗┓┏┓┃┗┫┣┛┃┏┓┃────┗┓┗┛┏┛ 
┃┃─┃┃─┃┃┃┃─┃┃─┃┗┛┗┓────┗┓┏┛─ 
┃┗━┛┃─┃┃┃┃─┃┃─┃┏━┓┃────┏┛┗┓─ 
┃┏━┓┃┏┛┗┛┃┏┫┣┓┃┗━┛┃───┏┛┏┓┗┓ 
┗┛━┗┛┗━━━┛┗━━┛┗━━━┛───┗━┛┗━┛
\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[1;32m
\033[1;32m┃ \033[37;41mFREE TOOL FOR HOT VEDIO\033[0;m\033 \033[1;32m ┃\033[1;32m  
\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[1;32m
""")
#------def-----#clear----#
def clear():
	os.system('clear')
	for c in adiib:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.012)
	x()
	print("[☠️] WONNER  : AHMED ADIB")
	print("[☠️] FB ID   : AHMED ADIB")
	print("[☠️] FB PAGE : HELLO WORLD ")
	x()
#------defmain-----#
def zoker():
	clear()
	sex()
	print(" [01] PLAY HOT VEDIO ")
	print(" [00] LOG OUT FROM TOOL")
	sex()
	option=input("[❤️‍🔥] \033[1;37mCHOICE ONE OPTION : > ")
	line()
	if option in ['01','1']:
		sex_vedio()
	else:
		print("{🖕} \033[1;36mFUCK YOUR SYSTEM")
#------vedioopen----#
def sex_vedio():
	clear()
	os.system("xdg-open https://t.me/hotvedio044")
#----end-----#
zoker()


	
	
	
