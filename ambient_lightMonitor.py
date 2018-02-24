#!/usr/bin/python

import os
import time
import RPi.GPIO as GPIO
import time
import datetime as dt
import Image, ImageStat
import math


GPIO.setmode(GPIO.BCM)

# brigtness functions inspired by:
# http://www.trevorappleton.blogspot.co.uk/2013/11/creating-time-lapse-camera-with.html

#Covert image to greyscale, return average pixel brightness
def brightness_GreyScaleMean():
   im = Image.open(imgFile).convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

#Covert image to greyscale, return RMS pixel brightness.
def brightness_GreyScaleRMS():
   im = Image.open(imgFile).convert('L')
   stat = ImageStat.Stat(im)
   return stat.rms[0]   

#Average pixels, then transform to "perceived brightness".
def brightness_Perceived():
   im = Image.open(imgFile)
   stat = ImageStat.Stat(im)
   r,g,b = stat.mean
   return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
   
def RCtime(PiPin):
  measurement = 0
  # Discharge capacitor
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(PiPin, GPIO.IN)
  # Count loops until voltage across
  # capacitor reads high on GPIO
  while (GPIO.input(PiPin) == GPIO.LOW):
    measurement += 1

  return measurement
  
  
def getFormattedTime():
    now = dt.datetime.now()
    return now.strftime("%d %b %Y %H:%M:%S")
  
def logtofile():	#log light levels
	myfile =open('lightLog.csv', 'a')
	myfile.write(getFormattedTime())
	myfile.write(',')
	myfile.write(str(RCtime(17)))
	myfile.write(',')
	myfile.write(str(brightness_GreyScaleMean()))
	myfile.write(',')
	myfile.write(str(brightness_GreyScaleRMS()))
	myfile.write(',')
	myfile.write(str(brightness_Perceived()))	
	myfile.write( '\n')
	myfile.close()
	
frameCount = 0
print 'Starting light level enumeration methods assessment....'
while frameCount < FRAMES:
	imageNumber = str(frameCount).zfill(7)
	print 'Assessing image number '+imageNumber
	os.system('raspistill -o '+imgFile)
	logtofile()
	frameCount += 1
	time.sleep(TIMEBETWEEN - 6)
