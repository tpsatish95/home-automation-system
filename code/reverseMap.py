import RPi.GPIO as GPIO
import time
# import MySQLdb
import sys
import urllib,json


'''
SCAN pins
15 - dev1 room1
19 - dev2 room1

21 - dev1 room2
23 - dev2 room2

24 - SCAN CLOCK
'''

room1 = [15,19]
room2 = [21,23]

rooms = [room1,room2]

### Init() Pi Board
GPIO.setmode(GPIO.BOARD)

pinListIn = [15, 19, 21, 23]
for i in pinListIn:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)


pinListIn = [15, 19, 21, 23]
for i in pinListIn:
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
    rNum = 1
    for i in rooms:
        dNum = 1
        for j in i:
            # Update DB
            updateStat(rNum, "Dev" + str(dNum), GPIO.input(j))
            dNum += 1
        rNum += 1

    time.sleep(1)
