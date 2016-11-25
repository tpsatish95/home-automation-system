import cherrypy
from cherrypy import tools
#import RPi.GPIO as GPIO
import time


### Init() Pi Board 
#GPIO.setmode(GPIO.BOARD)

devList = ["Dev1","Dev2","Dev3","Dev4","Dev5","Dev6","Dev7","Dev8"]
pinList = [7,11,12,13,15,16,18,22]
curStat = [0,0,0,0,0,0,0,0]

devStat = dict(zip(devList,curStat))
devPin = dict(zip(devList,pinList))

#for i in pinList: 
#    GPIO.setup(i, GPIO.OUT) 
        


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"
    
    @cherrypy.expose
    @tools.json_out()
    def controldevice(self,devNum=0,status=2):
        cherrypy.response.headers['Content-Type'] = "application/json"
        if devNum ==0 or status == 2:
            message = {"error" : "True", "status" : "Data Invalid!"}
            return message    
        
        # handle Rasp Pi Code
        
        if devStat[devNum] != status and status != 2:
            if devStat[devNum] == 0:
                #GPIO.output(devPin[devNum],GPIO.HIGH)
                devStat[devNum] = 1
                print(devNum+" Toggled to ON!")
                time.sleep(0.5)
            elif devStat[devNum] == 1:
                #GPIO.output(devPin[devNum],GPIO.LOW)
                devStat[devNum] = 0
                print(devNum+" Toggled to OFF!")
                time.sleep(0.5)
        else:
            print(devNum+" Toggled Already!")
        #GPIO.cleanup()
        message = {"devNum":devNum, "status" : status,"error" : "False", "message" : "Switch state changed!" }
        return message

if __name__ == '__main__':
   cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': 8002,})
   cherrypy.quickstart(HelloWorld())