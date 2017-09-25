from datetime import datetime as dt
from time import sleep

def sanitary(rgbcode):
   rgb = rgbcode[1:len(rgbcode)]
   rgbarray = rgb.split('.')
   return rgbarray

def toRGB(hexcode):
   return ".0.100.200"

def sunrise(riseTime):
  print("rgb: 0,0,0")
  print(dt.now().hour)
  riseTime = int(riseTime) - 1
  if(dt.now().hour == riseTime):
      sleep(600)
      print("rgb: 10,0,0")
      sleep(600)
      print("rgb: 50,0,0")
      sleep(300)
      print("rgb: 100,50,50")
      sleep(300)
      print("rgb: 255,100,100")

while(True):
   userInput = input()
   if(userInput[0] == '#'):
      print("hex: " + str(sanitary(toRGB(userInput))))
   elif(userInput[0] == '.'):
      print("rgb: " + str(sanitary(userInput)))
   elif(userInput == "War Eagle"):
      print("WDE")
   elif(userInput[0:7] == "sunrise"):
      sunrise(userInput[7:len(userInput)])
   else:
      continue
