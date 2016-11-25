import RPi.GPIO as GPIO
import time
# import MySQLdb
import sys
import urllib, json


'''
SCAN pins
19 - S0 (original s1)
15 - S1 (original s0)(Loop thru all devices)

21 - Z1 (Room 1)
23 - Z2 (Room 2)

24 - SCAN CLOCK
'''

### Init() Pi Board 
GPIO.setmode(GPIO.BOARD)

S0Pin = 19
S1Pin = 15

ROOM1Pin = 21
ROOM2Pin = 23 

pinListIN = [S0Pin,S1Pin]
for i in pinListIN: 
    GPIO.setup(i, GPIO.OUT)

pinListOUT = [ROOM1Pin,ROOM2Pin]
for i in pinListOUT: 
    GPIO.setup(i, GPIO.IN)

# # open DB Connection
# db = MySQLdb.connect(host=sys.argv[1], port=3306, user="root", passwd="", db="has")

# def updateStat(roomN, devNum, stat):
#     cursor = db.cursor()
#     cursor.execute("UPDATE room" + roomNum + "set status ="+ stat +" where devNum ='"+ devNum +"'")
#     return

def updateStat(roomN, devNum, stat):
	url = "http://"+sys.argv[1]+"/HAS/update.php?roomNum="+str(roomN)+"&devNum="+str(devNum)+"&status="+str(stat)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return

while 1:
	dev = 1
	for i in [GPIO.LOW,GPIO.HIGH]:
		for j in [GPIO.LOW,GPIO.HIGH]:	
			
			# Device Selection
			GPIO.output(S0Pin,i)                
			GPIO.output(S1Pin,j)

			# Update DB
			updateStat(1,"Dev" + str(dev), GPIO.input(ROOM1Pin))
			updateStat(2,"Dev" + str(dev), GPIO.input(ROOM2Pin))

			dev += 1
	time.sleep(3)
