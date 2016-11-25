import cherrypy
from cherrypy import tools
import RPi.GPIO as GPIO
import time
# import MySQLdb
import sys
import urllib, json

'''
APP Input pins
12 - S0
10 - S1 (Device Selection)

8 - Z1 (HIGH/LOW)
16 - Z2 (CLOCK)

(LOW 11 - Select Room 1/ LOW 18 - Select Room 2)
11 - ROOM 1
18 - ROOM 2

SCAN pins
19 - S0 (original s1)
15 - S1 (original s0)(Loop thru all devices)

21 - Z1 (Room 1)
23 - Z2 (Room 2)

24 - SCAN CLOCK
'''

### Init() Pi Board
GPIO.setmode(GPIO.BOARD)

S0Pin = 12
S1Pin = 10

Z1Pin = 8
Z2Pin = 16

ROOM1Pin = 11
ROOM2Pin = 18

pinList = [S0Pin,S1Pin,Z1Pin,Z2Pin,ROOM1Pin,ROOM2Pin]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)

devList = ["Dev1","Dev2","Dev3","Dev4"]
devConf = ["00","01","10","11"]

devPin = dict(zip(devList,devConf))

roomDict = dict()
roomDict["1"] = [GPIO.LOW,GPIO.HIGH]
roomDict["2"] = [GPIO.HIGH,GPIO.LOW]

def genClockInput():
    GPIO.output(Z2Pin,GPIO.LOW)
    time.sleep(1)
    GPIO.output(Z2Pin,GPIO.HIGH)

    GPIO.output(Z1Pin,GPIO.LOW)
    return

# # open DB Connection
# db = MySQLdb.connect(host=sys.argv[1], port=3306, user="root", passwd="", db="has")

def getStat(roomN, devNum):
    url = "http://"+sys.argv[1]+"/HAS/getstatus.php?roomNum="+str(roomN)+"&devNum="+str(devNum)
    response = urllib.urlopen(url);
    data = json.loads(response.read())
    return data["status"]

def updateStat(roomN, devNum, stat):
	url = "http://"+sys.argv[1]+"/HAS/update.php?roomNum="+str(roomN)+"&devNum="+str(devNum)+"&status="+str(stat)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	return

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    @tools.json_out()
    def controldevice(self,roomNum=0,devNum=0,status=2):

        cherrypy.response.headers['Content-Type'] = "application/json"

        if devNum ==0 or status == 2 or roomNum == 0:
	    print("error")
            message = {"error" : "True", "status" : "Data Invalid!"}
            return message

        # handle Rasp Pi Code

        STATUS = int(getStat(roomNum,devNum))
	print("Current status: "+ str(STATUS))

        if STATUS != status and status != 2:
            s0 = int(devPin[devNum][0])
            s1 = int(devPin[devNum][1])
            if s0 == 1:
                s0 = GPIO.HIGH
            elif s0 == 0:
                s0 = GPIO.LOW
            if s1 == 1:
                s1 = GPIO.HIGH
            elif s1 == 0:
                s1 = GPIO.LOW

            if STATUS == 0:

                # Select Room
                GPIO.output(ROOM1Pin,roomDict[roomNum][0])
                GPIO.output(ROOM2Pin,roomDict[roomNum][1])
		print roomDict[roomNum][0]

                # Set Device
                GPIO.output(S0Pin,s0)
                GPIO.output(S1Pin,s1)

                # Set Output
                GPIO.output(Z1Pin,GPIO.HIGH)

                # Genrate Clock
                genClockInput()

                updateStat(roomNum,devNum,1)
                print(devNum+" Toggled to ON!")
                time.sleep(1)

            elif STATUS == 1:

                # Select Room
                GPIO.output(ROOM1Pin,roomDict[roomNum][0])
                GPIO.output(ROOM2Pin,roomDict[roomNum][1])

                # Select Device
                GPIO.output(S0Pin,s0)
                GPIO.output(S1Pin,s1)

                # Set Output
                GPIO.output(Z1Pin,GPIO.LOW)

                # Genrate Clock
                genClockInput()

                updateStat(roomNum,devNum,0)
                print(devNum+" Toggled to OFF!")
                time.sleep(1)

        else:
            print(devNum+" Toggled Already!")
        #GPIO.cleanup()
        message = {"devNum":devNum, "status" : status,"error" : "False", "message" : "Switch state changed!" }
        return message

if __name__ == '__main__':
   cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': 8002,})
   cherrypy.quickstart(HelloWorld())
