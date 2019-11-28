from datetime import datetime as dt
from time import sleep
import pigpio

RED_PIN = 17
GREEN_PIN = 22
BLUE_PIN = 24

pi = pigpio.pi()

def setcolor(array):
   pi.set_PWM_dutycycle(RED_PIN, array[0])
   pi.set_PWM_dutycycle(GREEN_PIN, array[1])
   pi.set_PWM_dutycycle(BLUE_PIN, array[2])
   
def sanitary(rgbcode):
   rgb = rgbcode[1:len(rgbcode)]
   rgbarray = rgb.split('.')
   rgbarray = [int(x) for x in rgbarray]
   for i in range(0,3):
      if(rgbarray[i] < 0):
         rgbarray[i] = 0
      if(rgbarray[i] > 255):
         rgbarray[i] = 255
   return rgbarray

def toRGB(hexcode):
   hexcodeReal = hexcode[1:7]
   return "/" + "/".join(str(i) for i in tuple(int(hexCodeReal[i:i + len(hexCodeReal) // 3], 16) for i in range(0, len(hexCodeReal), len(hexCodeReal) // 3)))

def sunrise(riseTime):
  setColor([0,0,0])
  riseTime = int(riseTime) - 1
  if(dt.now().hour == riseTime):
      sleep(600)
      setColor([10,0,0])
      sleep(600)
      setColor([50,0,0])
      sleep(300)
      setColor([100,50,50])
      sleep(300)
      setColor([255,100,100])

def warEagle():
   try:
      while(True):
         pi.set_PWM_dutycycle(17,3)
         pi.set_PWM_dutycycle(22,36)
         pi.set_PWM_dutycycle(24,77)
         sleep(2.5)
         pi.set_PWM_dutycycle(17,221)
         pi.set_PWM_dutycycle(22,85)
         pi.set_PWM_dutycycle(24,156)
         sleep(2.5)
         pi.set_PWM_dutycycle(17,73)
         pi.set_PWM_dutycycle(22,110)
         pi.set_PWM_dutycycle(24,156)
         sleep(2.5)
         pi.set_PWM_dutycycle(17,246)
         pi.set_PWM_dutycycle(22,128)
         pi.set_PWM_dutycycle(24,38)
         sleep(2.5)
   except KeyboardInterrupt:
      pass
   
while(True):
   userInput = input()
   if(userInput[0] == '#'):
      setColor((sanitary(toRGB(userInput))))
   elif(userInput[0] == '.'):
      setColor(sanitary(userInput))
   elif(userInput == "War Eagle"):
      warEagle()
   elif(userInput[0:7] == "sunrise"):
      sunrise(userInput[7:len(userInput)])
   else:
      continue

pi.stop()
