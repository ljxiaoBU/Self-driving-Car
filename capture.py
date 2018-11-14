#!/usr/bin/env python
import pygame
import io
import time
import picamera
import picamera.array
import numpy as np
from carControl import carControl
import threading
import os
os.environ['SDL_VIDEODRIVER'] = 'x11'

global key
global isCapture
class SplitFrames(object):
	#global key
	def __init__(self):
		self.frame_num = 0
		self.output = None

	def write(self, buf):
		global key
		if buf.startswith(b'\xff\xd8'):
				# Start of new frame; close the old one (if any) and
				# open a new output
			if self.output:
				self.output.close()
			self.frame_num += 1
			self.output = io.open('/home/pi/Desktop/Project/photots/image7+%02d+%02d.jpg' % (self.frame_num,key), 'wb')
		self.output.write(buf)
def collect_thread():
	global key
	pygame.init()
	pygame.display.set_mode((100,100))
	car = carControl()
		
	while isCapture:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.KEYDOWN:
				input_key = pygame.key.get_pressed()
				if input_key[pygame.K_w]:
					car.carMoveForward()
					key = 1
					time.sleep(0.25)
				elif	input_key[pygame.K_s] == 1:
					car.carMoveBackward()
					key = 2
					time.sleep(0.25)
				elif	input_key[pygame.K_a] == 1:
					car.carTurnLeft()
					key = 3
					time.sleep(0.25)
				elif	input_key[pygame.K_d] == 1:
					car.carTurnRight()
					key = 4
					time.sleep(0.25)
				elif	input_key[pygame.K_q] == 1:
					car.cleanGPIO()
					key = 5
					time.sleep(0.25)
	car.cleanGPIO()		

def capture():
	global isCapture
	isCapture = True
	with picamera.PiCamera(resolution=(160,120), framerate=30) as camera:
		camera.start_preview()
		# Give the camera some warm-up time
		time.sleep(2)
		output = SplitFrames()
		start = time.time()
		camera.start_recording(output, format='mjpeg')
		camera.wait_recording(30)
		camera.stop_recording()
		finish = time.time()
		print('Captured %d frames at %.2ffps' % (
		output.frame_num,
		output.frame_num / (finish - start)))
	isCapture = False
if __name__ == '__main__':
	thread = threading.Thread(target = collect_thread, args = ())
	thread.setDaemon(True)
	thread.start()
	capture()
	
